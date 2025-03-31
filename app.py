# AI Dream Journal - By Aditi

import streamlit as st

st.title("🌙 AI Dream Journal by Aditi")
st.write("Describe your dream, and AI will generate an artwork based on it!")

dream_text = st.text_area("Enter your dream description:")

if st.button("Generate Dream Art"):
    st.write("🔮 AI is generating your dream-inspired artwork... (Feature coming soon!)")
