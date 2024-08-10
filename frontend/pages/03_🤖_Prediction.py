import os
import streamlit as st
import requests
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import pandas as pd
import datetime



st.set_page_config(
    page_title ='Predict Page',
    page_icon = "🤖",
    layout="wide"
)

# #load authentification credentials
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create an authentication object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)



# invoke the login authentication
name, authentication_status, username = authenticator.login()

# # Display the app content based on authentication status
if authentication_status is None:
     st.warning('Please Login with your username and password to access the app')
     test_code = """
            Guest Account
            Username:guestuser
            Password: selenium2025
            """
     st.code(test_code)
     
elif authentication_status == False:
    st.error('Username/password is incorrect')

else:
    # Logout User
    authenticator.logout('Logout', 'sidebar')


    # set title of the application
    st.title("Income Status Prediction 🤖")

    # load api endpoints 
    xgb_classifier_endpoint =  "http://127.0.0.1:8000/predict-income-status/xgb_classifier"
    gradient_boost_endpoint =  "http://127.0.0.1:8000/predict-income-status/gradient_boosting" 
        
        

    # select a model to use
    col1,col2 = st.columns(2)
    with col1:
        selected_model = st.selectbox("Select model to predict",options=["XGB Classifier","Gradient Boosting Algorithm"], key="selected_model")
            
    # initialize the session state
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "XGB Classifier"

    # Initialize session state for input feature keys
    input_keys = ["age", "gender", "education", "marital_status", "race", "is_hispanic", "employment_commitment", 
                "employment_stat", "wage_per_hour", "working_week_per_year", "industry_code", "industry_code_main", 
                "occupation_code", "occupation_code_main", "total_employed", "household_stat", "household_summary", 
                "vet_benefit", "tax_status", "gains", "losses", "stocks_status", "citizenship", "mig_year", 
                "country_of_birth_own", "country_of_birth_father", "country_of_birth_mother", 
                "migration_code_change_in_msa", "migration_code_move_within_reg", "migration_code_change_in_reg", 
                "residence_1_year_ago", "migration_prev_sunbelt", "importance_of_record"]

    numeric_keys = ["age", "employment_stat", "wage_per_hour", "working_week_per_year", 
                    "industry_code", "occupation_code", "total_employed", "gains", "losses",
                    "stocks_status", "mig_year", "vet_benefit", "importance_of_record"]
    for key in input_keys:
        if key not in st.session_state:
            if key in numeric_keys:
                st.session_state[key] = 0  # Initialize numeric keys with 0
            else:
                st.session_state[key] = ""

    

    # Define function to accept inputs and display forms
    def display_forms():
        with st.form(key="input_features"):
            col1, col2, col3 = st.columns(3)

            with col1:
                st.header("👤 Demographic Information Form")
                st.text_input("Please enter your ID", key="id")
                st.number_input("Please enter your age", min_value=0, max_value=120, step=1, key="age")
                st.selectbox("Please select your gender", options=["Male", "Female"], key="gender")
                st.selectbox("Please select your education", options=['High school graduate', '12th grade no diploma', 'Children',
                    'Bachelors degree(BA AB BS)', '7th and 8th grade', '11th grade', '9th grade', 'Masters degree(MA MS MEng MEd MSW MBA)',
                    '10th grade', 'Associates degree-academic program', '1st 2nd 3rd or 4th grade', 'Some college but no degree', 'Less than 1st grade',
                    'Associates degree-occup/vocational', 'Prof school degree (MD DDS DVM LLB JD)', '5th or 6th grade', 'Doctorate degree(PhD EdD)'], key="education")
                st.selectbox("Please select your marital status", options=['Widowed', 'Never married', 'Married-civilian spouse present',
                    'Divorced', 'Married-spouse absent', 'Separated', 'Married-A F spouse present'], key="marital_status")
                st.selectbox("Please select your race", options=['White', 'Black', 'Asian or Pacific Islander',
                    'Amer Indian Aleut or Eskimo', 'Other'], key="race")
                st.selectbox("Hispanic Status", options=['All other', 'Mexican-American', 'Central or South American',
                    'Mexican (Mexicano)', 'Puerto Rican', 'Other Spanish', 'Cuban', 'Chicano'], key="is_hispanic")
                st.selectbox("Select your citizenship Status", options=['Native', 'Foreign born- Not a citizen of U S', 'Foreign born- U S citizen by naturalization',
                    'Native- Born abroad of American Parent(s)', 'Native- Born in Puerto Rico or U S Outlying'], key="citizenship")
                st.selectbox("Select your country of birth", options=['US', 'El-Salvador', 'Mexico', 'Philippines', 'Cambodia', 'China',
                    'Hungary', 'Puerto-Rico', 'England', 'Dominican-Republic', 'Japan', 'Canada', 'Ecuador', 'Italy', 'Cuba', 'Peru', 'Taiwan', 'South Korea',
                    'Poland', 'Nicaragua', 'Germany', 'Guatemala', 'India', 'Ireland', 'Honduras', 'France', 'Trinadad&Tobago', 'Thailand', 'Iran', 'Vietnam',
                    'Portugal', 'Laos', 'Panama', 'Scotland', 'Columbia', 'Jamaica', 'Greece', 'Haiti', 'Yugoslavia', 'Outlying-U S (Guam USVI etc)',
                    'Holand-Netherlands', 'Hong Kong'], key="country_of_birth")
                st.selectbox("Select your father's country of birth", options=['US', 'India', 'Poland', 'Germany', 'El-Salvador', 'Mexico',
                    'Puerto-Rico', 'Philippines', 'Greece', 'Canada', 'Ireland', 'Cambodia', 'Ecuador', 'China', 'Hungary', 'Dominican-Republic', 'Japan', 'Italy',
                    'Cuba', 'Peru', 'Jamaica', 'South Korea', 'Yugoslavia', 'Nicaragua', 'Columbia', 'Guatemala', 'France', 'England', 'Iran', 'Honduras',
                    'Haiti', 'Trinadad&Tobago', 'Outlying-U S (Guam USVI etc)', 'Thailand', 'Vietnam', 'Hong Kong', 'Portugal', 'Laos', 'Scotland', 'Taiwan',
                    'Holand-Netherlands', 'Panama'], key="father_country_of_birth")
                st.selectbox("Select your mother's country of birth", options=['US', 'India', 'Peru', 'Germany', 'El-Salvador', 'Mexico',
                    'Puerto-Rico', 'Philippines', 'Canada', 'France', 'Cambodia', 'Italy', 'Ecuador', 'China', 'Hungary', 'Dominican-Republic', 'Japan', 'England',
                    'Cuba', 'Poland', 'South Korea', 'Yugoslavia', 'Scotland', 'Nicaragua', 'Guatemala', 'Holand-Netherlands', 'Greece', 'Ireland', 'Honduras',
                    'Haiti', 'Outlying-U S (Guam USVI etc)', 'Trinadad&Tobago', 'Thailand', 'Jamaica', 'Iran', 'Vietnam', 'Columbia', 'Portugal', 'Laos', 'Taiwan',
                    'Hong Kong', 'Panama'], key="mother_country_of_birth")
                st.selectbox("Tax Status", options=['Head of household', 'Single', 'Nonfiler', 'Joint both 65+', 'Joint both under 65', 'Joint one under 65 & one 65+'], key="tax_status")

            with col2:
                st.header("👔Employment Information")
                st.selectbox("Please select your employment commitment", options=['Not in labor force', 'Children or Armed Forces', 'Full-time schedules',
                    'PT for econ reasons usually PT', 'Unemployed full-time', 'PT for non-econ reasons usually FT', 'PT for econ reasons usually FT',
                    'Unemployed part-time'], key="employment_commitment")
                st.number_input("Please enter your employment status (1 Self Employed, 2 Unemployed, 3 Employed)", min_value=1, max_value=3, step=1, key="employment_stat")
                st.number_input("Please enter your wage per hour", min_value=0, max_value=200, step=1, key="wage_per_hour")
                st.number_input("What is your working week per year", min_value=0, max_value=56, step=1, key="working_week_per_year")
                st.number_input("Please enter your industry code", min_value=0, max_value=999, step=1, key="industry_code")
                st.selectbox("Which industry do you fall?", options=['Not in universe or children', 'Hospital services', 'Retail trade',
                    'Finance insurance and real estate', 'Manufacturing-nondurable goods', 'Transportation', 'Business and repair services',
                    'Medical except hospital', 'Education', 'Construction', 'Manufacturing-durable goods', 'Public administration', 'Agriculture',
                    'Other professional services', 'Mining', 'Utilities and sanitary services', 'Private household services',
                    'Personal services except private HH', 'Wholesale trade', 'Communications', 'Entertainment', 'Social services', 'Forestry and fisheries', 'Armed Forces'], key="industry_code_main")
                st.number_input("Please enter your occupation code", min_value=0, max_value=999, step=1, key="occupation_code")
                st.selectbox("Which occupation do you fall?", options=['Adm support including clerical', 'Other service',
                    'Executive admin and managerial', 'Sales', 'Machine operators assmblrs & inspctrs', 'Precision production craft & repair', 'Professional specialty',
                    'Handlers equip cleaners etc', 'Transportation and material moving', 'Farming forestry and fishing', 'Private household services',
                    'Technicians and related support', 'Protective services', 'Armed Forces'], key="occupation_code_main")
                st.number_input("How many times have you been employed?", min_value=0, max_value=20, step=1, key="total_employed")
                st.number_input("Please enter your gains from taxes", min_value=0, max_value=1000000, step=1, key="gains")
                st.number_input("Please enter your losses from taxes", min_value=0, max_value=1000000, step=1, key="losses")
                st.number_input("Please enter your Stocks status", min_value=0, max_value=1000000, step=1, key="stocks_status")

            with col3:
                st.header("🛂 Family and Immigration Information")
                st.selectbox("Household Status", options=['Householder', 'Nonfamily householder', 'Child 18+ never marr Not in a subfamily', 'Child <18 never marr not in subfamily', 'Spouse of householder',
                    'Child 18+ spouse of subfamily RP', 'Secondary individual', 'Child 18+ never marr RP of subfamily', 'Other Rel 18+ spouse of subfamily RP',
                'Grandchild <18 never marr not in subfamily', 'Other Rel <18 never marr child of subfamily RP', 'Other Rel 18+ ever marr RP of subfamily',
                    'Other Rel 18+ ever marr not in subfamily', 'Child 18+ ever marr Not in a subfamily', 'RP of unrelated subfamily', 'Child 18+ ever marr RP of subfamily',
                    'Other Rel 18+ never marr not in subfamily', 'Child under 18 of RP of unrel subfamily', 'Grandchild <18 never marr child', 'Grandchild <18 never marr child of subfamily RP',
                    'Grandchild 18+ never marr not in subfamily', 'Other Rel <18 never marr not in subfamily', 'In group quarters', 'Grandchild 18+ ever marr not in subfamily',
                    'Other Rel 18+ never marr RP of subfamily', 'Child <18 never marr RP of subfamily', 'Grandchild 18+ never marr RP of subfamily', 'Spouse of RP of unrelated subfamily',
                    'Grandchild 18+ ever marr RP of subfamily', 'Child <18 ever marr not in a subfamily', 'Child <18 ever marr RP of subfamily', 'Other Rel <18 ever marr RP of subfamily',
                    'Grandchild 18+ spouse of subfamily RP', 'Child <18 spouse of subfamily RP', 'Other Rel <18 ever marr not in subfamily', 'Other Rel <18 never married RP of subfamily',
                    'Other Rel <18 spouse of subfamily RP', 'Grandchild <18 ever marr not in subfamily', 'Grandchild <18 never marr RP of subfamily'], key="household_stat")
                
                st.selectbox("Household Summary", options=['Householder', 'Child 18 or older', 'Child under 18 never married', 'Spouse of householder',
                    'Nonrelative of householder', 'Other relative of householder', 'Group Quarters- Secondary individual', 'Child under 18 ever married'], key="household_summary")
                
                
                st.selectbox("Select your Migration Code", options=['unchanged', 'MSA to MSA', 'NonMSA to nonMSA', 'MSA to nonMSA', 'Not identifiable', 
                    'NonMSA to MSA', 'Abroad to MSA', 'Abroad to nonMSA'], key="migration_code_change_in_msa")
                
                st.selectbox("Select your Migration Code Within Region", options=['unchanged', 'Same county', 'Different state in South', 'Different county same state',
                    'Different state in West', 'Different state in Northeast', 'Abroad', 'Different state in Midwest'], key="migration_code_move_within_reg")
                
                st.selectbox("Select your Migration Code Change in Region", options=['unchanged', 'Same county', 'Different state same division',
                    'Different county same state', 'Different region', 'Abroad', 'Different division same region'], key="migration_code_change_in_reg")
                
                st.selectbox("Have you changed Residence in a year ago?", options=['Same', 'No'], key="residence_1_year_ago")
                
                st.selectbox("Do you have migration Previous Sunbelt", options=['Same', 'No'], key="migration_prev_sunbelt")
                st.number_input("Enter your Migration Year (94 or 95)", min_value=94, max_value=95, step=1, key="mig_year")
                st.number_input("Veterans Benefits (1- 'Yes', 2- 'No', 3- 'Not sure')", min_value=1, max_value=3, step=1, key="vet_benefit")
                st.number_input("Please enter the Importance of Record", min_value=0, max_value=1000, key="importance_of_record")

                # Add form submit button
                submit_button = st.form_submit_button("Make Prediction", type="primary", use_container_width=True)
        return submit_button

    # Define function to make prediction
    def make_prediction():
        input_features = {key: st.session_state[key] for key in input_keys}
        # Check if the selected model is XGB Classifier
        if st.session_state["selected_model"] == "XGB Classifier":
            # Send api response to the XGB classifier api
            response = requests.post(xgb_classifier_endpoint, json=input_features)
        else:
            response = requests.post(gradient_boost_endpoint, json=input_features)
        if response.status_code == 200:
            result = response.json()
            # print the prediction
            model_used = result.get("model_used")
            prediction = result.get("prediction")
            probability = result.get("prediction_probability")
            st.divider()
            st.success(f"Your Income status is {prediction} with a probability of {probability}")
            return input_features, model_used,prediction, probability
        
        else:
            st.error(f"Error: {response.json()["error"]}")
            return None, None

    def save_predictions():
        input_features, model_used, prediction, probability = make_prediction()
        # Get the timestamp of prediction
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        input_features["model_used"] = model_used
        input_features["prediction"] = prediction
        input_features["probability"] = probability
        input_features["prediction_time"] =  timestamp

        # Load existind data if it exists
        if os.path.exists("prediction_history.csv"):
            history_df = pd.read_csv("prediction_history.csv")
        else:
            history_df = pd.DataFrame()

        # Convert the new prediction to a DataFrame
        new_entry_df = pd.DataFrame([input_features])

        # Append the new prediction to the history
        history_df = pd.concat([history_df,new_entry_df], ignore_index=True)
        # export df as prediction_history.csv
        history_df.to_csv('../data/prediction_history.csv',mode="a", header=not os.path.exists('../data/prediction_history.csv'),index=False)
        
    

    if __name__ == "__main__":
        # call the display form function
        submit_button = display_forms()
        # Make predictions if submit button is clicked
        if submit_button:
            save_predictions()

    