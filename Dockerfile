FROM python:3.8.18

COPY .env .
COPY ./src/ .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "app.py"]