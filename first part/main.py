import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")
animal_type = st.sidebar.selectbox("Whast is youe pet?",("Cat","Dog","Cow","Hen"))

pet_color = st.sidebar.text_area(label=f"What is the color of your {animal_type}?",max_chars=15)

if pet_color:
    response = lch.generate_pet_name(animal_type,pet_color)
    st.text(response)  