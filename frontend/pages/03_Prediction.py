import os
import streamlit as st
import pandas as pd
import joblib
import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
#from catboost import CatBoostClassifier


st.set_page_config(
    page_title ='Predict Page',
    layout="wide"
)

# Display the app content based on authentication status
if st.session_state['authentication_status']== None:
    st.warning('Please login from the home page')
elif st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status']:

    st.title("Predict Churn!")
    # load the machine learning model
    @st.cache_resource()
    def load_ml_components():
        with open("../models/model_components.joblib","rb") as file:
            model_components = joblib.load(file)
        return model_components

    model_components = load_ml_components()


    # load model components
    catboost_model = model_components["catboost_model"]
    logistic_regressor = model_components["log_regression"]
    sgb_classifier = model_components["sgb_classifier"]


    # initialize the session state

    if "selected_model" not in st.session_state:
        st.session_state.selected_model = "Catboost" 
    # select a model to use
    col1,col2 = st.columns(2)
    with col1:
        selected_model = st.selectbox("Select model to predict",
                                                    options=["Catboost","Logistic Regression","SGB", "XGboost", "Random Forest"],
                                                    key="selected_model",
                                                    index=["Catboost","Logistic Regression","SGB", "XGboost", "Random Forest"].index(st.session_state.selected_model))
    st.write("#")
    # Update the session state based on the selected model
    selected_model = st.session_state.selected_model


    # select a model from the select_box
    @st.cache_resource(show_spinner="loading models...")
    def get_selected_model(selected_model):
        if selected_model == "Catboost":
            pipeline =  catboost_model
        elif selected_model == "Logistic Regression":
            pipeline =  logistic_regressor
        else:
            pipeline =  sgb_classifier
        encoder = model_components["encoder"]
        return pipeline, encoder


    # write a function to make prediction
    def make_prediction(pipeline,encoder):
        gender = st.session_state["gender"]
        age = st.session_state["age"]
        education = st.session_state["education"]
        marital_status = st.session_state["marital_status"]
        race = st.session_state["race"]
        is_hispanic = st.session_state["is_hispanic"]
        employment_commitment = st.session_state["employment_commitment"]
        employment_stat = st.session_state["employment_stat"]
        wage_per_hour = st.session_state["wage_per_hour"]
        working_week_per_year = st.session_state["working_week_per_year"]
        industry_code = st.session_state["industry_code"]
        industry_code_main = st.session_state["industry_code_main"]
        occupation_code = st.session_state["occupation_code"]
        occupation_code_main = st.session_state["occupation_code_main"]
        total_employed = st.session_state["total_employed"]
        household_stat = st.session_state["household_stat"]
        household_summary = st.session_state["household_summary"]
        vet_benefit = st.session_state["vet_benefit"]
        tax_status = st.session_state["tax_status"]
        gains = st.session_state["gains"]
        losses = st.session_state["losses"]
        stocks_status = st.session_state["stocks_status"]
        citizenship = st.session_state["citizenship"]
        tax_status = st.session_state["tax_status"]
        country_of_birth_own = st.session_state["country_of_birth_own"]
        country_of_birth_father = st.session_state["country_of_birth_father"]
        country_of_birth_mother = st.session_state["country_of_birth_mother"]
        migration_code_change_in_msa = st.session_state["migration_code_change_in_msa"]
        migration_prev_sunbelt = st.session_state["migration_prev_sunbelt"]
        migration_code_move_within_reg = st.session_state["migration_code_move_within_reg"]
        mig_year = st.session_state["mig_year"]
        migration_code_change_in_reg = st.session_state["migration_code_change_in_reg"]
        residence_1_year_ago = st.session_state["residence_1_year_ago"]


        
        # create rows for the dataframe
        data=[[age, gender, education, marital_status, race, is_hispanic,
       employment_commitment, employment_stat, wage_per_hour,working_week_per_year, industry_code, industry_code_main,
       occupation_code, occupation_code_main, total_employed,household_stat, household_summary, vet_benefit, tax_status,gains, losses, stocks_status, citizenship, mig_year,
       country_of_birth_own, country_of_birth_father,country_of_birth_mother, migration_code_change_in_msa,migration_prev_sunbelt, migration_code_move_within_reg,migration_code_change_in_reg, residence_1_year_ago]]
        # create columns for the dataframe
        columns = ['age', 'gender', 'education', 'marital_status', 'race', 'is_hispanic',
       'employment_commitment', 'employment_stat', 'wage_per_hour',
       'working_week_per_year', 'industry_code', 'industry_code_main',
       'occupation_code', 'occupation_code_main', 'total_employed',
       'household_stat', 'household_summary', 'vet_benefit', 'tax_status',
       'gains', 'losses', 'stocks_status', 'citizenship', 'mig_year',
       'country_of_birth_own', 'country_of_birth_father',
       'country_of_birth_mother', 'migration_code_change_in_msa',
       'migration_prev_sunbelt', 'migration_code_move_within_reg',
       'migration_code_change_in_reg', 'residence_1_year_ago',
       'importance_of_record', 'age_group']
        df = pd.DataFrame(data=data,columns=columns)

        # make predictions
        pred = pipeline.predict(df)
        pred_int = int(pred[0])

        # transform the predicted variable 
        prediction = encoder.inverse_transform([[pred_int]])[0]

        # calculate prediction probability
        probability = pipeline.predict_proba(df)[0][pred_int]

        # Map probability to Yes or No
        prediction_label = "Yes" if pred_int == 1 else "No" 

        # update the session state with the prediction and probability
        st.session_state["prediction"] = prediction
        st.session_state["prediction_label"] = prediction_label
        st.session_state["probability"] = probability
        
        # update the dataframe to capture predictions for the history page
        df["PredictionTime"] = datetime.date.today()
        df["ModelUsed"] = st.session_state["selected_model"]
        df["Prediction"] = st.session_state["prediction"]
        df["PredictionProbability"] = st.session_state["probability"]
        # export df as prediction_history.csv
        df.to_csv('./dataset/prediction_history.csv',mode="a", header=not os.path.exists('./dataset/prediction_history.csv'),index=False)
        return prediction,prediction_label,probability

    # create an 

    if "prediction" not in st.session_state:
        st.session_state.prediction = None

    if "probability" not in st.session_state:
        st.session_state.probability = None


    # write a function to show the forms to accepts input
    def display_forms():
        # call the get_selected_model function
        pipeline,encoder = get_selected_model(st.session_state.selected_model)

        with st.form('input-features', clear_on_submit=True):
            col1,col2 = st.columns(2)
            with col1:
                st.write("## Personal Information")
                st.selectbox("Select your gender",options=["Male","Female"],key="gender")
                st.selectbox("Are you a senior citizen?",options=[0,1],key="senior_citizen")
                st.selectbox("Do you have a dependent ?",options=["Yes","No"],key="dependents")
                st.selectbox("Do you have a partner?",options= ["Yes", "No",],key="partner")
                st.number_input("Enter your tenure",min_value = 0, max_value = 72,step=1, key="tenure")
                st.number_input("Enter your monthly charges",min_value=0.00, max_value = 200.00,step=0.10, key="monthly_charges")
                st.number_input("Enter you total charges per year",min_value=0.00,max_value=100000.00, step=0.10,key="total_charges")
                st.selectbox("Select your prefered contract type",options=["Month-to-month","One year","Two year"],key="contract")
                st.selectbox("Select your payment method",options= ["Electronic check", "Mailed check","Bank transfer (automatic)",
            "Credit card (automatic)"], key="payment_method")
            with col2:
                st.write("### Service Information")
                st.selectbox("Do you have a phone service?",options=["Yes","No"],key="phone_service")
                st.selectbox("Do you have a multiple lines?",options=["Yes","No"],key="multiple_lines")
                st.selectbox("Which internet service do you prefer ?",options= ["Fiber optic", "No", "DSL"],key="internet_service")
                st.selectbox("Have you subscribed to our online security service?",options=["Yes","No"],key="online_security")
                st.selectbox("Have you subscribed to our online backup service?",options=["Yes","No"],key="online_backup")
                st.selectbox("Have you subscribed to our device protection service?",options=["Yes","No"],key="device_protection")
                st.selectbox("Have you subscribed to our tech support service?",options=["Yes","No"],key="tech_support")
                st.selectbox("Have you subscribed to our streaming TV service?",options=["Yes","No"],key="streaming_tv")
                st.selectbox("Have you subscribed to our streaming movies service?",options=["Yes","No"],key="streaming_movies")
                st.selectbox("Have you subscribed to our Paperless Billing Service?",options=["Yes","No"],key="paperless_billing")
            st.form_submit_button("Make Prediction",on_click=make_prediction,kwargs=dict(pipeline=pipeline,encoder=encoder))



        

    if __name__ == "__main__":
        
        # call the display_forms function
        display_forms()
        #st.write(st.session_state)

        final_prediction = st.session_state["prediction"]
        if not final_prediction:
            st.write("## Prediction shows here")
            st.divider()
        else:
            # display the prediction result result
            col1,col2 = st.columns(2)
            with col1:
                st.write("### Prediction Results")
                st.write(st.session_state["prediction"])
            with col2:
                st.write("### Prediction Probability")
                probability = st.session_state['probability']*100
                st.write(f"{probability:.2f}%")