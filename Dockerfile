FROM python:3.8-slim-buster

WORKDIR /github_crawler
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD [ "python","main.py"]
