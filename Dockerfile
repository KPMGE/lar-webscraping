FROM python:3.10.4-alpine3.14

WORKDIR /usr/lar-webscraping

RUN pip install requests && pip install beautifulsoup4 && pip install lxml

COPY . /usr/lar-webscraping/

CMD [ "python", "./script/main.py" ]
