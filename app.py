import streamlit as st
import requests
from src import logger

st.title("Movie Recommendation")

movie = st.text_input("Enter a movie name", max_chars=30, placeholder="movie name")

if movie:

    api_url = f"http://127.0.0.1:8000/query?movie={movie}"

    try:
        response = requests.get(url= api_url)
        data = response.json()
        st.write("API Response:")
        st.write(data)
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        st.error("Issue occured")
