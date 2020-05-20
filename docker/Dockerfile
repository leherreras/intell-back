FROM python:3.6-buster

COPY /src /src/
WORKDIR /src
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
