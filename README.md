# News Article Summarizer 🗞

## Credits
The project was developed by:
- Kévin Chok
- David Garcia
- Samba Marega
- Franck Pietka

## Context and Goals 🎯
The way news and information are spread throughout the world has changed dramatically in the last few decades. The newspaper was for decades, if not centuries, the predominating media tool. That has changed since the early 2000's, first with the internet and then with social media, which has become the default
news-spreading technique. It is also a fact that the audience wants information to be quick and precise. Precisely that is the purpose of this project:
to use AI to give the audience timely and accurate summarized news articles, so they can be informed in a quick and reliable manner.

## Tech Stack 📡
In order to develop the project, we relied on different resources and technologies, which will be listed below.

* Training data: 3,800 BBC news articles in english, that includes the original and summarized versions of the articles
  Link to dataset:
  https://www.kaggle.com/datasets/pariza/bbc-news-summary
* Python - Backend (algorithms, data analysis, machine learning)
* Streamlit - Frontend (graphs and user interface)
* FastAPI - API development
* Docker - Containerization

## Use Guide and Local Deployment
In order to use our API it is necessary to follow the following steps:

Requirements:
- Have Docker installed
- Have a browser installed (preferrably Google Chrome)

#### 1. Download files.
- Go to your terminal and enter the following command:
  git clone https://github.com/davidegc1/FinalProject_NewsSummarizer.git
- This will download a folder named _FinalProject_NewsSummarizer_

#### 2. Launch API
- Go to the downloaded folder and open it.
  
- **Build image**: First, it is necessary to build the image. You can do so by entering the folder _FastAPI_, which is inside _FinalProject_NewsSummarizer_. Right-click that folder and select "_New Terminal at Folder_". There is a file called _run.sh_, open it. You should run the first command on your terminal, which goes:
docker build . -t bbc_api_image

- **Launch image**: Once the image is built, run it locally with the following command:
  docker run -it -v "$(pwd):/home/app" -p 8080:8080 bbc_api_image

- The API documentation can now be seen in your browser in the following link:
  http://localhost:8080/docs

Note: The whole process might take up to 10 to 20 minutes.

#### 3. Launch hosted API
- In order to use the API in the website it is necessary to launch the streamlit app, you should follow the same steps as before, but
  we will use the *bbc_news* folder and it will be deployed on the 4000 port.

- Open *bbc_news* folder

- **Build image**: Open new terminal in the *bbc_news* folder and run the first command:
  docker build . -t bbc_streamlit_image
  
- **Launch image**: After it is done, run the second command to launch the image locally:
  docker run -it -v "$(pwd):/home/app" -p 4000:4000 bbc_streamlit_image

- After that command is done, open the following link in your browser:
  http://localhost:4000/

#### Done! After following the tutorial both the API and the Web application should be running on your computer.
 
  


