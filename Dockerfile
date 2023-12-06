FROM ubuntu:latest
RUN apt-get update && apt-get upgrade
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y pulseaudio
RUN apt-get install -y alsa-base alsa-utils libsndfile1-dev

RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=US/Central
RUN apt-get install -y python3-tk 


WORKDIR /app
COPY . /app

RUN python3 -m pip install -r requirements.txt
RUN python3 -m spacy download en
CMD ["python3", "./art-project-main/main.py"]