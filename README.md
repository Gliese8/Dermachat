docker build -t django_project .
docker run -it -p 8000:8000 -v ~/.aws:/root/.aws django_project
