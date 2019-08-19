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
c++:
  - crow
  - pistache
kotlin:
  - ktor
R:
  - plumber
```

# Benchmarking tools

<a href="https://github.com/wg/wrk/" target="_blank">wrk</a>

# Tests

Since <em>application/json</em> is the most used API reponse type, json serialization is being tested.

## Hello World!

## API json contract

The API response is expected as:

```json
{"data": "Hello World!"}
```