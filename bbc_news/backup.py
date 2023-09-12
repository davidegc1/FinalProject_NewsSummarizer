import streamlit as st
import pandas as pd
import requests
from transformers import BartForConditionalGeneration, BartTokenizer
import torch
import requests


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

# FastAPI
# app = FastAPI()
# @app.get("/")


# Model
def summarize_text(text_inp):
    # Load BART model and tokenizer
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    # Preprocess the text
    inputs = tokenizer.batch_encode_plus(         [text_inp],         max_length=1024,         truncation=True,         padding="longest",         return_tensors="pt"     )
    #   Generate the summary
    summary_ids = model.generate(
        inputs['input_ids'],
        num_beams=4,
        max_length=150,
        early_stopping=True     )
    summary = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)
    return summary

# if __name__=="__main__":
    # uvicorn.run(app, host="0.0.0.0", port=4000)

# Submit button
if st.button('Submit'):
        # Display output
        st.subheader("Summarized Article")
        output = summarize_text(text_inp)
        st.write(output)
        st.divider()


        # Make calculations for benefits
        words_per_minute = 238 # avg words per minute for adult
        before = len(text_inp.split()) # amount of words in input
        after = len(output.split()) # amount of words in output
        
        time_article = round(before/words_per_minute,2)
        time_summary = round(after/words_per_minute,2)
        time_saved = time_article - time_summary
        difference = before / after

        # Make columns
        col1, col2 = st.columns(2)
        with col1:  
        # Display benefits
            st.subheader("Benefits of using the App")
            st.write("Before:", before, "words.")
            st.write("After:", after, "words.")
            st.write("The average reader saves", time_saved, "minutes with the summary.")
            st.write("The summary is", difference, "times shorter than the original article.")    

        with col2:
        # Display download options
            st.subheader("Download")
            st.download_button("TXT", mime="txt", data=output, file_name="article_summary.txt")
            st.download_button("DOC", mime="doc", data=output, file_name="article_summary.doc")
            st.download_button("PDF", mime="pdf", data=output, file_name="summary.pdf")