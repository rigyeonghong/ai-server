FROM python:3

WORKDIR /app

RUN pip3 install flask

RUN pip3 install keras

RUN pip3 install tensorflow --no-cache-dir

RUN pip3 install Pillow

COPY . /app

CMD ["python3", "app.py"]