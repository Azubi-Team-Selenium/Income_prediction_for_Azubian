#Import libraries
import streamlit as st 
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


#set page configuration
st.set_page_config(
    page_title = "Home Page",
    page_icon ="🏠",
    layout = "wide"
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
    st.write(f'Welcome *{username}*')
    # Logout User
    authenticator.logout('Logout', 'sidebar')

    st.title("Home")
    #define function to get animation
    def lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None                 
        return r.json()

    
    video_url = lottie_url("https://lottie.host/4daa3a00-5997-4968-8167-dbda109a159b/hTqEP6E4eV.json")

    mach_img = lottie_url("https://lottie.host/f3cc30b8-c8a9-4ff9-b098-badb339f1156/ey8S2pPCHT.json")

    

    lottie_img = lottie_url("https://lottie.host/9f50ad42-37fa-48db-870c-74b018740507/3i0ws9t1Di.json")

    lottie_home = lottie_url("https://lottie.host/688abbd4-b507-4a63-867a-66b08b13eda1/pQtDrgPxsS.json")

    st.sidebar.markdown("Hi!")

    selected = option_menu(None, options=["Why Income IQ", "About Us", "Explore", "Get in Touch"], 
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
                     st_lottie(
        video_url,
        speed=0.05,
        reverse= False,
        loop=True,
        quality="high",
        key="lottieani",
        height=300,
        width=400

    )
        st.write("---")

        cola, colb = st.columns(2)
        with colb:
            st.write("##")
            st.markdown("""
                    **Income IQ** is your go-to tool for estimating your potential income based on various personal and professional factors.""")
            st.write("##")
            st.markdown("""
                    Whether you are a recent graduate, a mid-career professional, or planning for retirement, our app provides valuable insights to help you make informed financial decisions.""")
        with cola:
            st.image("https://img.freepik.com/free-vector/blue-gradient-technology-background_23-2149112673.jpg")
        st.write("---")
        colc, cold = st.columns(2)
        with colc:
            st.markdown("""### Key Features""")
                        
            st.markdown("""
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


    if selected == "Get in Touch":
            st.header("Get In Touch With Us!")
            with st.container():
                col1, col2 = st.columns([2,1])
                with col1:




                    contact_form = """
                    <form action="https://formsubmit.co/adubrightkwarrteng11@gmail,com" method="POST">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="text" name="name" placeholder="Your name" required>
                        <input type="email" name="email" placeholder="Your email" required>
                        <textarea name="message" placeholder="Your message here"></textarea>
                        <button type="submit">Send</button>
                    </form>
                    """

                    st.markdown(contact_form, unsafe_allow_html=True)

                    # Use Local CSS File
                    def local_css(file_name):
                        with open(file_name) as f:
                            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


                    local_css("./style/style.css")

                with col2:
                        st_lottie(
                    lottie_img,
                    speed=0.05,
                    reverse= False,
                    loop=True,
                    quality="high",
                    key="coding",
                    height=300,
                    width=300)
                st.write("""
            If you have any questions or need assistance, feel free to reach out to our support team at [support@incomeiq.com](mailto:incomeiq@gmail.com).""")
                        
                
                st.write("---")
                st.write("##")

            
            with st.container():
                        st.header("""Privacy and Security""")
                        st.write("""Your privacy is our priority. All data entered into the Income IQ is securely stored and handled with the utmost confidentiality.
            """)
                        st.write("##")
                        st.write("##")
                
                        st.write("""


            ## Thank you for choosing Income IQ. 
                                 
             We are excited to help you plan for a brighter financial future!
            """
            )
    if selected == "Explore":
            col1, col2 = st.columns([2,1])
            with col1:    
                st.markdown("""### Getting Started""")
                st.markdown(""" To begin, simply navigate to the 'Input Data' section and fill in your details. The more accurate your information, the better the predictions we can provide.""")
                st.markdown("""We use two powerful machine learning algorithms for prediction. They include:""")
                st.markdown("""
                            1. XGB Classifier - 95% accuracy

                            2. Gradient Boosting Algorithm - 94% accuracy
                            """)
        
                st.markdown("""### How Our Prediction App Works""")
                st.markdown("""
                1. **Enter Your Details:** Provide information such as age, education level, employment status, and other relevant details.
                2. **Submit Your Data:** Click the 'Make Prediction' button to get your income estimation.
                3. **View Results:** Review your predicted income and explore the detailed analysis provided in real time!.
                            
                ### **Want to give feedback or discuss your options?**""")
                st.markdown("""Get in touch""")

            with col2:
                st_lottie(
                mach_img,
                speed=0.05,
                reverse= False,
                loop=True,
                quality="high",
                key="lottieanime",
                height=300,
                width=400

            )
                st.write("##")
            
            
                