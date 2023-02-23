FROM python:3.10-slim-buster
WORKDIR /app
COPY ../requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ml.py ml.py

ENV DATA=https://homepages.dcc.ufmg.br/~cunha/hosted/compsci401-s3-23-datasets/playlist-sample-ds1.csv

CMD [ "python3", "ml.py"]