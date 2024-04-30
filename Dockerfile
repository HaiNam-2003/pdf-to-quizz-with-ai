FROM ubuntu:latest

RUN apt update && apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.10 && \
    apt install pip
WORKDIR /app

COPY . .
CMD ["sleep", "infinity"]   