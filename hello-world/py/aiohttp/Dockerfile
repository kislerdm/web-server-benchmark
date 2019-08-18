FROM python:3.7.4-slim-stretch AS build

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY . .

RUN python -m pip install --no-cache-dir -r requirements.txt \
  && pyinstaller --clean --distpath ./ -F -n run_server api.py \
  && rm -rf __pycache__ api.py

FROM alpine:edge AS serve

COPY --from=build /app /

ENTRYPOINT ./run_server