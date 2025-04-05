# streamlit_app.py
import streamlit as st
from package_sort import sort

st.title('Package Classification')

st.header('Enter the dimensions and mass of the package:')
width = st.number_input('Width (in cm)', min_value=0)
height = st.number_input('Height (in cm)', min_value=0)
length = st.number_input('Length (in cm)', min_value=0)
mass = st.number_input('Mass (in kg)', min_value=0)

if st.button('Classify'):
    if isinstance(width, (int, float)) and isinstance(height, (int, float)) and isinstance(length, (int, float)) and isinstance(mass, (int, float)):
        classification = sort(width, height, length, mass)
        st.write(f'The package is classified as: {classification}')
    else:
        st.write('Please enter valid numeric values for all fields.')