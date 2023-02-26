FROM python:3.9

COPY .  /app

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN pip install numpy

RUN pip install -r requirements.txt


ENTRYPOINT FLASK_APP=/app/App.py flask run
