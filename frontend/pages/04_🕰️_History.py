import os
import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


st.set_page_config(
    page_title ='History Page',
    page_icon="🕰️",
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

    def display_history_page():
            # get the path of the history data
            csv_path = "../data/prediction_history.csv"
            if os.path.exists(csv_path):
                history_data= pd.read_csv(csv_path, delimiter=",")
                st.dataframe(history_data)
            else:
                st.write("No history data found")
                st.write("Please run the app and make a prediction to view the history page")
                st.stop()

    if __name__ == "__main__":
         st.title("History Page🕰️")
         display_history_page()
