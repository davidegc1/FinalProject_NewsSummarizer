FROM continuumio/miniconda3

WORKDIR /home/app

RUN apt-get update -y 
RUN apt-get install nano unzip
RUN apt-get install -y python3.10
RUN apt install curl -y

RUN curl -fsSL https://get.deta.dev/cli.sh | sh

# COPY requirements.txt /dependencies/requirements.txt
# RUN pip install -r /dependencies/requirements.txt
RUN pip install fastapi pydantic transformers torch uvicorn

COPY . /home/app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]