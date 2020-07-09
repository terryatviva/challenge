# This dockerfile is used to build product_reviews_backend

ARG BUILD_DATE
ARG VCS_REF

#Pull base image
FROM python:3.7.3

MAINTAINER Allu Aravind <alluaravind1313@gmail.com>

ADD . /code/
WORKDIR /code
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN pip install -r ./requirements/test.txt
