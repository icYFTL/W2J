FROM python:3

RUN mkdir /opt/app
WORKDIR /opt/app

COPY config.json core.py W2J.py requirements.txt ./
COPY source ./source/
COPY lib_dwebp ./lib_dwebp/
RUN pip3 install -r requirements.txt
RUN chmod +x ./lib_dwebp/linux/dwebp