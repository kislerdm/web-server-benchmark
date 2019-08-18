FROM node:12.8.0-alpine AS build

WORKDIR /app

COPY . .

RUN yarn && yarn add express

CMD node api.js