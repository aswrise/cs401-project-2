FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py app.py
EXPOSE 30505
ENV VERSION=2
CMD [ "python3", "-m" , "flask", "run", "--host", "0.0.0.0", "--port", "30505"]