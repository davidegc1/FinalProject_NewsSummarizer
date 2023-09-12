from fastapi import FastAPI
from pydantic import BaseModel
from transformers import BartForConditionalGeneration, BartTokenizer
import torch
import sys

# create api instance
description = """
API used to summarize any news article, to less than 150 words. Topics vary from business, entertainment, sports, politics and technology.  

## Endpoints 
* _predict_ - summarizes the news article
"""

app = FastAPI(
    title="News Article Summarizer API",
    description=description
)

# get endpoint
@app.get("/test")
async def index():
    return 'Welcome to our News Summarizer API! To get the most out of it add "/docs" at the end of the current link, so you can get an idea of how it works.'

# define model
class TextRequest(BaseModel):
    text: str

model_name = "facebook/bart-large-cnn"
print('model_name', model_name)
sys.stdout.flush()

# Load BART model and tokenizer
tokenizer = BartTokenizer.from_pretrained(model_name)
print('tokenizer',tokenizer)
sys.stdout.flush()

model = BartForConditionalGeneration.from_pretrained(model_name)
print('model', model)
sys.stdout.flush()

# define function that summarizes text
async def summarize_text(text_inp):
    """
    Instructions: copy and paste your news article in the below area.
    """
  
    # Preprocess the text
    inputs = tokenizer.batch_encode_plus([text_inp],max_length=1024, truncation=True, padding="longest", return_tensors="pt")
    print('preprocessing', inputs)
    sys.stdout.flush()

    # Generate the summary
    summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=150, early_stopping=True)
    print('summary_ids',summary_ids)
    sys.stdout.flush()

    summary = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)
    print('summary', summary)
    sys.stdout.flush()

    return summary

# predict endpoint
@app.post('/predict')
async def predict(request: TextRequest):
    # Obtenez le texte à résumer à partir de la requête
    text = request.text
    print('text', text)
    sys.stdout.flush()
    # Utilisez Gensim pour générer le résumé du texte
    summary = await summarize_text(text)
    # Retournez le résumé généré en tant que réponse JSON
    return {'predict': summary}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=4002, timeout_keep_alive=240,limit_max_request_size=524288000)