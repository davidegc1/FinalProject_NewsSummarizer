FROM python

WORKDIR /home/app

RUN pip install transformers boto3 pandas streamlit scikit-learn torch uvicorn
COPY . /home/app

CMD streamlit run --server.port 4000 app.py