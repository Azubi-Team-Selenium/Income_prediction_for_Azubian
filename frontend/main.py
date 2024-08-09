#get libraries
import streamlit as st 
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import os
#import yaml
#from yaml.loader import SafeLoader
#import streamlit_authenticator as stauth

#set page configuration
st.set_page_config(
    page_title= "Home Page",layout = 'wide'
)

#load authentification credentials
#with open('./config.yaml') as file:
    #config = yaml.load(file, Loader=SafeLoader)


#define function to get animation
def lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None                 
    return r.json()
video_file = open("./images/AR-metaball.mp4", "rb")
video_bytes = video_file.read()
video_url = "https://ar-website-assets.s3.eu-west-3.amazonaws.com/AR-metaball.mp4"

logo_path = "./images/second.png"

lottie_img = lottie_url("https://lottie.host/80d6a368-c787-4f59-8eca-9b649cf41b1b/VdfzfJeXsp.json")

lottie_home = lottie_url("https://lottie.host/56f1fdb0-7195-4d5e-ab49-1beb911cc968/GZnG6lXfIu.json")

st.sidebar.markdown("Hi!")
with st.sidebar:
    st.logo(logo_path)

selected = option_menu(None, options=["Why PayPredict", "About Us", "Upload", "Get in Touch"], 
    icons=['house','gear', 'cloud-upload'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected
#intro talking about title 
if selected == "Why PayPredict":
    st.write("")
    st.write("")
    st.markdown("# People. Economy. AI")
    col,img_col = st.columns([2,1])
    with col:
        st.write("---")
        st.markdown(""" #### Founded in 2024, PayPredict is the 21st-century tech-enabled services company transforming how companies are built and run. Our unique approach, enabled by our process orchestration platform, secures a seamless integration of technology and talent. """)
        st.markdown("""
                #### With our app, you can:
                - #### Use our powerful machine learning models to predict customer churn without hassle and in real time
                - #### Make data driven decisions effortlessly""")
        
    with img_col:
        st.video(video_file, loop=True, autoplay=True, muted=True)
        #st.image(".images/gif.gif")
if selected == "About Us":
    col1, col2 = st.columns(2)
    with col1:
        st.title("About us")
        st.write("#### We are leading professionals with a diverse portfolio range⭐⭐⭐⭐⭐")
        st.markdown("""
                #### **Income Predictor** is your go-to tool for estimating your potential income based on various personal and professional factors. Whether you are a recent graduate, a mid-career professional, or planning for retirement, our app provides valuable insights to help you make informed financial decisions.

### Key Features
- **User-Friendly Interface:** Easy to navigate and input your data.
- **Accurate Predictions:** Our advanced algorithms analyze your input to provide precise income predictions.
- **Personalized Insights:** Get tailored advice based on your unique profile.
- **Comprehensive Data Analysis:** Explore detailed breakdowns of your predicted income and the factors influencing it.

### How It Works
1. **Enter Your Details:** Provide information such as age, education level, employment status, and other relevant details.
2. **Submit Your Data:** Click the 'Predict' button to get your income estimation.
3. **View Results:** Review your predicted income and explore the detailed analysis provided.

### Getting Started
To begin, simply navigate to the 'Input Data' section and fill in your details. The more accurate your information, the better the predictions we can provide.

### Privacy and Security
Your privacy is our priority. All data entered into the Income Predictor is securely stored and handled with the utmost confidentiality.

### About Us
Income Predictor is developed by a team of data scientists and financial experts committed to helping individuals achieve their financial goals through data-driven insights.

### Contact Us
If you have any questions or need assistance, feel free to reach out to our support team at [support@example.com](mailto:support@example.com).

Thank you for choosing Income Predictor. We are excited to help you plan for a brighter financial future!
""")
    with col2:
        st_lottie(
    lottie_home,
    speed=1,
    reverse= False,
    loop=True,
    quality="high",
    key="coding",
    height=500,
    width=600

)

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