# Pull the node image from Docker Hub

FROM node:9-alpine
MAINTAINER Allu Aravind <alluaravind1313@gmail.com>

WORKDIR /usr/src/app
RUN npm install
COPY . .
RUN npm run build
