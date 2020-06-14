FROM alpine:3.7
MAINTAINER Maciej Kofel
RUN apk update --no-cache && apk add python3 \
python2-dev \
py2-pip \ 
git \
bash

RUN git clone https://github.com/szkolasecurity/blind_xss_demo.git
WORKDIR blind_xss_demo
RUN pip2 install -r requirements.txt
CMD [ "python2", "./app.py" ]