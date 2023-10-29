import streamlit as st
import pickle
import pandas as pd
import base64
import json 
import requests 
# from streamlit_lottie import st_lottie 


# Load the trained model 
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)




def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
# st.set_page_config(
#     page_title="Water Inlet Classification",
#     page_icon=":droplet:",
#     layout="wide",
    
# )

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    backdrop-filter: blur(1000px);
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
# Set page title and description
import streamlit as st

# Set page title with white border
st.markdown("<p style=\"text-align: center; color: black; font-size: 60px; font-family: 'Times New Roman', Times, serif; text-stroke: 15px white;\">Classification of PEM Fuel Cell</p>", unsafe_allow_html=True)

# Description with white border
st.markdown("<p style=\"font-family: 'Times New Roman', Times, serif; color: black; font-weight: bold; font-size: 34px; text-align: center; -webkit-text-stroke: 0px white;\">This app classifies the state of Fuel Cell based on Current and water inlet values based on a trained model.</p>", unsafe_allow_html=True)


# path = "C:\\Users\\Suyash Tambe\\Desktop\\PDS\\Animation - 1697974655236.json"

# with open(path,"r") as file: 
#     url = json.load(file)

# st_lottie(url, 
#     reverse=True, 
#     height=100, 
#     width=700, 
#     speed=1, 
#     loop=True, 
#     quality='high', 
    
    
# )

# Sidebar for user input
# st.header('Water Inlet Classification')

water_inlet_1 = st.number_input("Water Inlet 1", min_value=0.0, max_value=5000.0, step=1.0)

water_inlet_2 = st.number_input("Water Inlet 2", min_value=0.0, max_value=5000.0, step=1.0)

current = st.number_input("Current",min_value=0.0,max_value=500.0, step=1.0)

set_background(r'drop-of-water-578897.jpg')



# Predict function
def predict(water_inlet_1, water_inlet_2):
    input_data = pd.DataFrame({'primary water inlet pressure 1': [water_inlet_1], 'primary water inlet pressure 2': [water_inlet_2]})
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        return "faulty(1)"
    else:
        return "normal(0)"

# Prediction and display
result = None

# Prediction and display with custom background color
if st.button('Predict'):
    result = predict(water_inlet_1, water_inlet_2)

# Custom background color for success message
if result is not None:
    st.markdown(
        f"""
        <div style="background-color: teal; padding: 10px; border-radius: 10px;">
            <p style="color: white; font-size: 18px;">The predicted classification value  is {result}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
