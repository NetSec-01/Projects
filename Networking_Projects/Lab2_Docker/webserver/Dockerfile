FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
EXPOSE 8000 8080
ENTRYPOINT ["python3", "-m", "http.server", "8000"]

