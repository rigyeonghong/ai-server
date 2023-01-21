FROM python:3

WORKDIR /app

RUN pip3 install flask

RUN pip3 install selenium

RUN pip3 install webdriver_manager

RUN pip3 install shortuuid

RUN pip3 install boto3

RUN apt-get -y update

RUN apt install wget

RUN apt install unzip 

# RUN pip3 install gunicorn

# RUN pip3 install gevent

RUN pip3 install keras

RUN pip3 install Pillow

RUN pip3 install tensorflow --no-cache-dir

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt -y install ./google-chrome-stable_current_amd64.deb

RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/` curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

RUN mkdir chrome

RUN unzip /tmp/chromedriver.zip chromedriver -d /app/chrome

COPY . /app

CMD ["python3", "app.py"]