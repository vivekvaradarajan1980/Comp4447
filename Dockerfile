FROM python:3.9
COPY .  /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD flask run -h 0.0.0.0 -p 5000
