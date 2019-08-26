# Web-servers benchmark

Benchmarking webservers built using different languages and libraries

```yaml
python:
  - aiohttp
  - sanic
  - tornado
  - falcon
  - flask
  - werkzeug
golang:
  - net/http
nodejs:
  - express
R:
  - plumber
julia:
  - Genie
```

# Benchmarking tools

<a href="https://github.com/wg/wrk/" target="_blank">wrk</a>

## Hardware/Enviroment

Tests were performed on a GCP <em>g1-small</em> machine, configs:

```yaml
instance:
  - type: g1-small
  - os-image: debian-cloud/debian-9-stretch-v20190813
  - cpu: Intel(R) Xeon(R) CPU @ 2.00GHz
  - ram: 1.7G
```

## Software

```yaml
python:
  - version: 3.7.4
  - libs:
    - aiohttp: 3.5.4
    - sanic: 19.6.3
    - tornado: 6.0.3
    - flask: 1.1.1
    - falcon: 2.0.0
    - werkzeug: 0.15.5
    - gunicorn: 19.9.0
go: 
  - version: 1.12.9
  - libs: 
    - net/nttp
nodejs:
  - version: 
  - libs: 
    - net/nttp: 
r:
  - version: 3.6.1
  - libs:
    - plumber: 
julia:
  - version: 1.1.1
  - libs:
    - Genie: 
```

# Tests

Since <em>application/json</em> is the most used API reponse type, json serialization is being tested.

## Hello World!

## API json contract

The API response is expected as:

```json
{"data": "Hello World!"}
```

