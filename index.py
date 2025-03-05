import streamlit as st
import random
from constants import QUOTES

# Streamlit UI
st.title("📖 Personalized Daily Quote App")
st.write("Get an inspiring quote based on your mood!")

# User Input
name = st.text_input("Enter your name:")
mood = st.selectbox("How are you feeling today?", ["happy", "sad", "motivated"])

# Generate Quote
if st.button("Get Quote"):
    if name and mood:
        quote = random.choice(QUOTES[mood])
        st.success(f"Hey {name}, here’s your quote: \n\n*{quote}*")
    else:
        st.warning("Please enter your name and select a mood.")