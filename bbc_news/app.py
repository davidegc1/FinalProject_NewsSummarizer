import streamlit as st
import pandas as pd
import requests
from transformers import BartForConditionalGeneration, BartTokenizer
import torch
import requests
import uvicorn


# Configuration
st.set_page_config(
    page_title="News Summarizer",
    page_icon="📰",
    layout="wide"
    )

##Title
st.title("News Article Summarizer🗞")

# Explain app in a few words
st.subheader("Copy and paste any news article and obtain a summarized version in just a few sentences!")

# Article input area
text_inp = st.text_area("Paste your article here:")

# Model
def summarize_text(text_inp):
    print(text_inp)
    print(type(text_inp))
    api_input = {"text": text_inp}
    r = requests.post("http://host.docker.internal:8080/predict", json=api_input)
    st.write(r.json())
    # json=api_input
    # params=api_input

# Submit button
if st.button('Submit'):
        # Display output
        st.subheader("Summarized Article")
        output = summarize_text(text_inp)
        st.write(output)