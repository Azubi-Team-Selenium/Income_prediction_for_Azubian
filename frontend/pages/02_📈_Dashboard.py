import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
        page_title="Dashboard",
        page_icon="📈",
        layout="wide",)

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


    st.title('Dashboard Page')
    st.markdown('This page provides visuals on Univariate, Bivariate, Multivariate, and KPIs analysis')

    # Load the data using pandas
    train_data = pd.read_csv('./data/training_df.csv')

    # Set default session state values if they don't exist
    if 'visualization_category' not in st.session_state:
        st.session_state.visualization_category = "Univariate Analysis"

    # Use session state to store the selection
    # Adjust the column widths for the selectbox and visualization area
    selectbox_column, visualization_column = st.columns([2, 3])  # Give more space to the selectbox
    st.session_state.visualization_category = selectbox_column.selectbox(
        "Select Visualization Category",
        ["Univariate Analysis", "Bivariate Analysis", "Multivariate Analysis", "KPIs"],
        index=["Univariate Analysis", "Bivariate Analysis", "Multivariate Analysis", "KPIs"].index(st.session_state.visualization_category)
    )

    # Add columns to the dashboard page
    col1, col2 = st.columns(2)

    # Custom color palette
    custom_palette = px.colors.qualitative.Pastel

    # Seaborn color palette
    seaborn_palette = sns.color_palette(custom_palette, as_cmap=True)

    # Color scale for plots
    color_scale = 'Viridis'

    if st.session_state.visualization_category == "Univariate Analysis":
        with col1:
            age_df = px.histogram(train_data, x='age', nbins=10, title='Age Distribution')
            age_df.update_layout(xaxis_title='Age', yaxis_title='Frequency')
            age_df.update_traces(marker_color=custom_palette[0])
            st.plotly_chart(age_df, use_container_width=True)
            age_df.update_layout(template="plotly_dark")

            gender_df = px.histogram(train_data, x='gender', title='Gender Distribution')
            gender_df.update_layout(xaxis_title='Gender', yaxis_title='Count', xaxis={'categoryorder': 'total descending'})
            gender_df.update_traces(marker_color=custom_palette[1])
            st.plotly_chart(gender_df, use_container_width=True)
            gender_df.update_layout(template="plotly_dark")

        with col2:
            marital_df = px.histogram(train_data, x='marital_status', title='Marital Status Distribution')
            marital_df.update_layout(xaxis_title='Distribution of Marital Status', yaxis_title='Count',
                               xaxis={'categoryorder': 'total descending'})
            marital_df.update_traces(marker_color=custom_palette[2])
            st.plotly_chart(marital_df, use_container_width=True)
            marital_df.update_layout(template="plotly_dark")

            race_df = px.histogram(train_data, x='race', title='Race Distribution')
            race_df.update_layout(xaxis_title='Distribution of Race', yaxis_title='Count',
                               xaxis={'categoryorder': 'total descending'})
            race_df.update_traces(marker_color=custom_palette[2])
            st.plotly_chart(race_df, use_container_width=True)
            race_df.update_layout(template="plotly_dark")

    elif st.session_state.visualization_category == "Bivariate Analysis":
        with col1:
            # Create a box plot of age vs. income level using Plotly
            fig = px.box(
                train_data,
                x='income_above_limit',
                y='age',
                color='income_above_limit',
                title='Age vs. Income Level',
                labels={'income_above_limit': 'Income Level', 'age': 'Age'},
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig.update_layout(
                xaxis_title='Income Level',
                yaxis_title='Age',
                boxmode='overlay',
                legend_title='Income Level'
            )
            st.plotly_chart(fig, use_container_width=True)

            # Create a count plot of gender vs. income level using Plotly
            fig = px.histogram(
                train_data,
                x='gender',
                color='income_above_limit',
                title='Gender vs. Income Level',
                labels={'gender': 'Gender', 'income_above_limit': 'Income Level'},
                color_discrete_sequence=px.colors.qualitative.Pastel,
                category_orders={'gender': train_data['gender'].unique()}  # Order categories as in the data
            )
            fig.update_layout(
                xaxis_title='Gender',
                yaxis_title='Count',
                legend_title='Income Level'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Create a count plot of race vs. income level using Plotly
            fig = px.histogram(
                train_data,
                x='race',
                color='income_above_limit',
                barmode='group',
                title='Race vs. Income Level',
                labels={'race': 'Race', 'count': 'Count'},
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig.update_layout(
                xaxis_title='Race',
                yaxis_title='Count',
                xaxis={'categoryorder': 'total descending'},
                legend_title='Income Level'
            )
            st.plotly_chart(fig, use_container_width=True)

            # Create a count plot of marital_status vs. income_above_limit using Plotly
            fig = px.histogram(
                train_data,
                x='marital_status',
                color='income_above_limit',
                barmode='group',
                title='Marital Status vs. Income Level',
                labels={'marital_status': 'Marital Status', 'count': 'Count'},
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            fig.update_layout(
                xaxis_title='Marital Status',
                yaxis_title='Count',
                xaxis={'categoryorder': 'total descending'},
                legend_title='Income Level'
            )
            st.plotly_chart(fig, use_container_width=True)

    elif st.session_state.visualization_category == "Multivariate Analysis":
        selected_features = ['age', 'wage_per_hour', 'working_week_per_year', 'gains', 'losses']
        multivariate = sns.pairplot(train_data[selected_features])
        multivariate.fig.suptitle('Pair Plot of Selected Numerical Variables')
        st.pyplot(multivariate)

    elif st.session_state.visualization_category == "KPIs":
        with col1:
            st.markdown(
                f"""
                <div style="background-color: #4d4d00; border-radius: 10px; width: 80%; margin-top: 20px;">
                    <h3 style="margin-left: 30px">Quick Stats About Dataset</h3>
                    <hr>
                    <h5 style="margin-left: 30px"> Income Above Limit Rate: {(train_data['income_above_limit'].value_counts
                    (normalize=True).get("Above limit", 0) * 100):.2f}%.</h5>
                    <hr>
                    <h5 style="margin-left: 30px"> Income Below Limit Rate: {(train_data['income_above_limit'].value_counts
                    (normalize=True).get("Below limit", 1) * 100):.2f}%.</h5>
                    <hr>
                    <h5 style="margin-left: 30px">Average Age: {train_data['age'].mean():.2f}</h5>
                    <hr>
                    <h5 style="margin-left: 30px">Average Working week per Year: {train_data['working_week_per_year'].mean():.2f}</h5>
                    <hr>
                    <h5 style="margin-left: 30px"> Total Population: {train_data['age'].count()}</h5>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            pass
    
