import streamlit as st 
import pandas as pd
import time
from Utils.data_dict import markdown1
from Utils.data_dict import markdown2
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader



st.set_page_config(
    page_title= "Data Page", layout="wide"
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


   
    train_df = pd.read_csv("../data/training_df.csv")
    #grouping all numeric columns
    numerics = train_df.select_dtypes("number").columns
    categoricals = train_df.select_dtypes("object").columns


    #create a progress bar to let user know data is loading
    progress_bar = st.progress(0)
    for perc_completed in range(100):
        time.sleep(0.03)
        progress_bar.progress(perc_completed+1)

    st.success("Data loaded successfully!")

    # col1,col2 = st.columns(2)
    # with col1:
    option = st.selectbox(
        "How would you like to view data?",
        ("All data", "Numerical columns", "Categorical columns"),
        index=None,
        placeholder="Select view method...",)

    # Conditionally display data based on the selected option
    if option == "All data":
        st.write("### All Data")
        st.dataframe(train_df)
        if st.button("Click here to get more information about data dictionary"):
            col3,col4 = st.columns(2)
            with col3:
            # Display the markdown table inside the expander
                st.markdown(markdown1)
            with col4:
                st.markdown(markdown2)
            
    elif option == "Numerical columns":
        st.write("### Numerical Columns")
        numerics = train_df.select_dtypes("number").columns
        st.dataframe(train_df[numerics])
        if st.button("Click here to get more information about data dictionary"):
            # Display the markdown table inside the expander
            col3,col4 = st.columns(2)
            with col3:
            # Display the markdown table inside the expander
                st.markdown(markdown1)
            with col4:
                st.markdown(markdown2)
            
    elif option == "Categorical columns":
        st.write("### Categorical Columns")
        categoricals = train_df.select_dtypes("object").columns
        st.dataframe(train_df[categoricals])
        if st.button("Click here to get more information about data dictionary"):
            # Display the markdown table inside the expander
            col3,col4 = st.columns(2)
            with col3:
            # Display the markdown table inside the expander
                st.markdown(markdown1)
            with col4:
                st.markdown(markdown2)

        