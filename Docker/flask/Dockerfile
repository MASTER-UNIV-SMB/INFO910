FROM python:3.7.2-stretch

WORKDIR /src
ADD . /src

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]