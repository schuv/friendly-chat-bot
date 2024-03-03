FROM python:3.8.18

WORKDIR /build/

COPY requirements.txt /build/
COPY .env /build/

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

COPY . /build/

CMD ["python3", "app.py"]