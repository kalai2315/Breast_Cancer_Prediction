import streamlit as st
import pandas as pd
import numpy as np
import pickle
from streamlit_option_menu import option_menu

# Load the trained model
#model_filename = 'F:\project\BreastCancer_project\svm_model.pkl'
with open(svm_model.pkl, 'rb') as file:
    svm_model = pickle.load(file)


def setting_bg():
    st.markdown(f""" 
    <style>.stApp {{
        background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROTXXUyfONmFcq9TY2r8_i45f0UQBDEM3uWg&s")
        background-size: cover
    }}
    </style>
    """, unsafe_allow_html=True)

# Set the background image
setting_bg()

# Function to display the home page
def home_page():
    st.markdown("<h1 style='text-align: center;font-size: 36px; color: black;'>Breast Cancer Diagnosis Prediction</h1>", unsafe_allow_html=True)
    st.image("https://t3.ftcdn.net/jpg/06/70/97/26/360_F_670972635_dO3ZpqJbEtx2amrTgUrVTFXhJWes2tQq.jpg", use_column_width=True)
    
    st.markdown("""
    This application allows you to predict whether a breast cancer tumor is **benign** or **malignant** based on certain diagnostic features.
    
    Use the navigation menu to go to the **User Input Features** page and enter the required parameters to get a prediction.
    """)

# Function to display the user input features page
def user_input_features_page():
    st.title("Breast Cancer Diagnosis Prediction")
    st.markdown("""
    Enter the values for the following features to get a prediction:
    """)

    # Sidebar for user inputs
    st.sidebar.header('User Input Features')

    def user_input_features():
        perimeter_mean = st.sidebar.slider('Perimeter Mean', 0.0, 200.0, 100.0)
        area_mean = st.sidebar.slider('Area Mean', 0.0, 2500.0, 500.0)
        area_se = st.sidebar.slider('Area SE', 0.0, 100.0, 20.0)
        perimeter_worst = st.sidebar.slider('Perimeter Worst', 0.0, 300.0, 150.0)
        area_worst = st.sidebar.slider('Area Worst', 0.0, 4000.0, 1000.0)
        
        data = {
            'perimeter_mean': perimeter_mean,
            'area_mean': area_mean,
            'area_se': area_se,
            'perimeter_worst': perimeter_worst,
            'area_worst': area_worst
        }
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    # Display user inputs
    st.subheader('User Input Parameters')
    st.write(input_df)

    # Prediction button
    if st.button("Predict"):
        

        # Make a prediction
        prediction = svm_model.predict(input_df)

        # Display the result
        st.subheader('Prediction')
        if prediction[0] == 1:
            st.write("The prediction is: **Malignant**")
        else:
            st.write("The prediction is: **Benign**")



# Create the sidebar menu
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Home", "User Input Features"],
        icons=["house", "input-cursor"],
        menu_icon="cast",
        default_index=0,
    )

# Display the selected page

if selected == "Home":
    home_page()
elif selected == "User Input Features":
    user_input_features_page()
