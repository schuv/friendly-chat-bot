FROM python:3.8.18

WORKDIR /build/

COPY .env /build/
COPY ./src/ /build/

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "app.py"]