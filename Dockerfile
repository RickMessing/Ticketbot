FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY go /usr/app/src

CMD ["python3", "/main.py"]