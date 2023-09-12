docker build . -t bbc_streamlit_image
docker run -it -v "$(pwd):/home/app" -p 4000:4000 bbc_streamlit_image