# AI Dream Journal - By Aditi

import streamlit as st  
import requests  

# App Title  
st.title("🌙 AI Dream Journal by Aditi")  
st.write("Describe your dream, and AI will generate an analysis and artwork for it!")  

# User Input for Dream Description  
dream_text = st.text_area("Enter your dream description:")

# Hugging Face API for AI Text Generation (Dream Interpretation)  
def generate_dream_analysis(dream):  
    API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-3B"  
    headers = {"Authorization": "Bearer hf_xxx"}  # Replace xxx with your Hugging Face API key  

    response = requests.post(API_URL, headers=headers, json={"inputs": dream})  
    return response.json().get("generated_text", "No analysis available.")  

# Hugging Face API for AI Image Generation (Dream Art)  
def generate_dream_art(dream):  
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"  
    headers = {"Authorization": "Bearer hf_xxx "}  # Replace xxx with your Hugging Face API key  

    response = requests.post(API_URL, headers=headers, json={"inputs": dream})  
    return response.json()["generated_text"]  

# Button to Generate AI Analysis & Art  
if st.button("Generate AI Dream Journal"):  
    with st.spinner("Generating dream analysis..."):  
        analysis = generate_dream_analysis(dream_text)  
        st.subheader("Dream Meaning:")  
        st.write(analysis)  

    with st.spinner("Generating dream-inspired artwork..."):  
        art_url = generate_dream_art(dream_text)  
        st.image(art_url, caption="Dream-Inspired AI Art")

