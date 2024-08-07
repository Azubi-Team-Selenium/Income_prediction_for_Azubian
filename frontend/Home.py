#get libraries
import streamlit as st 
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import os
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

#set page configuration
st.set_page_config(
    page_title= "Home Page",layout = 'wide'
)

# #load authentification credentials
# with open('../config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['pre-authorized']
# )
# name, authentication_status, username = authenticator.login()

# # = authenticator.login('Login', 'main')



# # Display the app content based on authentication status
# if st.session_state['authentication_status'] == None:
#     st.warning('Please enter your username and password')
#     st.code("""
#             Guest Account
#             Username: brkwuser
#             Password: selenium2025""")
# elif st.session_state['authentication_status'] == False:
#     st.error('Username/password is incorrect')
# elif st.session_state['authentication_status']:
#     st.write(f'Welcome *{name}*')
#     #st.title('Some content')
#     authenticator.logout('Logout', 'sidebar')


#define function to get animation
def lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None                 
    return r.json()
video_file = open("../images/AR-metaball.mp4", "rb")
video_bytes = video_file.read()
video_url = "https://ar-website-assets.s3.eu-west-3.amazonaws.com/AR-metaball.mp4"

logo_path = "../images/second.png"

lottie_img = lottie_url("https://lottie.host/80d6a368-c787-4f59-8eca-9b649cf41b1b/VdfzfJeXsp.json")

lottie_home = lottie_url("https://lottie.host/688abbd4-b507-4a63-867a-66b08b13eda1/pQtDrgPxsS.json")

st.sidebar.markdown("Hi!")
with st.sidebar:
    st.logo(logo_path)

selected = option_menu(None, options=["Why Income IQ", "About Us", "Upload", "Get in Touch"], 
    icons=['house','gear', 'cloud-upload'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected
#intro talking about title 
if selected == "Why Income IQ":
    st.write("")
    st.write("")
    
    col,img_col = st.columns([2,1])
    with col:
        st.write("")
        st.write("")
        st.title(" People . Economy . AI")
        st.write(" The first of many steps towards Business Simplicity")
        st.write("")
        st.write("")
        st.button("Get in Touch", type="primary")
        
        
    with img_col:
        st.video(video_file, loop=True, autoplay=True, muted=True)
    st.write("---")

    cola, colb = st.columns(2)
    with colb:
        st.markdown("""
                **Income IQ** is your go-to tool for estimating your potential income based on various personal and professional factors.""")
        st.markdown("""
                Whether you are a recent graduate, a mid-career professional, or planning for retirement, our app provides valuable insights to help you make informed financial decisions.""")
    with cola:
        st.image("https://img.freepik.com/free-vector/blue-gradient-technology-background_23-2149112673.jpg")
    st.write("---")
    colc, cold = st.columns(2)
    with colc:
        st.markdown("""### Key Features
- **User-Friendly Interface:** Easy to navigate and input your data.
- **Accurate Predictions:** Our advanced algorithms analyze your input to provide precise income predictions.
- **Personalized Insights:** Get tailored advice based on your unique profile.
- **Comprehensive Data Analysis:** Explore detailed breakdowns of your predicted income and the factors influencing it."""
            
        )
    with cold:
        st.image("https://en.idei.club/uploads/posts/2023-06/1687164524_en-idei-club-p-blue-technology-background-dizain-pinteres-2.png")
    st.write("---")          
        
if selected == "About Us":
    col1, col2 = st.columns(2)
    with col1:
        st.write("")
        st.write("")
        st.markdown(""" Income IQ is the 21st-century tech-enabled app service founded in 2024, transforming how companies are built and run. Our unique approach, enabled by our operational and meticulous environment structure, secures a seamless integration of technology and talent. """)
        st.write("")
        st.write("")
        st.markdown("""
                Our vision is of a financial system that sets the global economy on a path of unlimited success. Our mission is to enable financial institutions or individuals to identify, quantify, track, and compare income profiles """)
        
        ### How It Works
# 1. **Enter Your Details:** Provide information such as age, education level, employment status, and other relevant details.
# 2. **Submit Your Data:** Click the 'Predict' button to get your income estimation.
# 3. **View Results:** Review your predicted income and explore the detailed analysis provided.
# """)
        
# ### Getting Started
# To begin, simply navigate to the 'Input Data' section and fill in your details. The more accurate your information, the better the predictions we can provide.

# ### Privacy and Security
# Your privacy is our priority. All data entered into the Income Predictor is securely stored and handled with the utmost confidentiality.

# ### Contact Us
# If you have any questions or need assistance, feel free to reach out to our support team at [support@example.com](mailto:support@example.com).

# Thank you for choosing Income Predictor. We are excited to help you plan for a brighter financial future!
# """)
    with col2:
        st_lottie(
    lottie_home,
    speed=0.05,
    reverse= False,
    loop=True,
    quality="high",
    key="coding",
    height=300,
    width=600

)
    st.write("---") 
    st.write("Meet the team")
    st.markdown("Income IQ is developed by a team of data scientists and financial experts committed to helping individuals achieve their financial goals through data-driven insights.")


    suc, bri, flo = st.columns(3)
    with bri:
        st.image("https://media.licdn.com/dms/image/v2/D4D03AQGLJT6dlGTlxw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1722374512323?e=1728518400&v=beta&t=l10xzb3Uny6JgZiLo6-MO63jaqXvaoZ1eMXUSM06NvQ",caption="Bright Adu Kwarteng Snr, Data Scientist/ Engineer ")
    with suc:
        st.image("https://media.licdn.com/dms/image/D4D03AQEsDHfqPIRdIA/profile-displayphoto-shrink_800_800/0/1692947993959?e=1728518400&v=beta&t=JQK4xY3q2uMZ5S1-1ixQNN7BVbsa_J2dLBpZJEo5zM0", caption="Success Makafui Kwawu, Data Scientist/ Engineer ")
    with flo:
        st.image("https://media.licdn.com/dms/image/C5603AQEJ5VeEx6GG4g/profile-displayphoto-shrink_800_800/0/1573488995134?e=1728518400&v=beta&t=F9mcaHJZiXa4LFxZkeubQaplljp5CE_1DTiuqibU4xk", caption="Florence Josephina, Data Scientist/Frontend Developer ")

#st.image()


if selected == "Upload":
        st.title("Explore?")
        st.markdown("""
                    #### We use our three powerful machine learning algorithms models to predict the risk of churn:
                    -  ##### Catboost
                    - ##### Logistic Regression
                    - ##### SQB
                    #### Want to try out with your own dataset? Say less!
                    #### Just upload here in one click!""")
        data_button = st.button("Upload your data",key="data")
        if data_button:
                switch_page("Bulk_Prediction")  