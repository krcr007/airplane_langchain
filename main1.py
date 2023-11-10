import streamlit as st
from langchian_helper1 import generate_details

st.title("Airplane checking system")

source = st.text_input("Enter source:")
destination = st.text_input("Enter destination:")
date = st.text_input("Enter date (YYYY-MM-DD):")

if st.button("Generate Details"):
    if source and destination and date:
        result = generate_details(source, destination, date)
        st.write(result)
    else:
        st.warning("Please enter source, destination, and date.")
