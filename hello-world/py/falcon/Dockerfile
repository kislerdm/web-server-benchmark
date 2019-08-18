FROM python:3.7.4-slim-stretch AS build

WORKDIR /app

COPY . .

RUN python -m pip install --no-cache-dir -r requirements.txt

ENV HOST 0.0.0.0
ENV PORT 4500

CMD gunicorn -b "${HOST}:${PORT}"