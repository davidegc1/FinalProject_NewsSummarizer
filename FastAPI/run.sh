docker build . -t bbc_api_image
docker run -it -v "$(pwd):/home/app" -p 8080:8080 bbc_api_image