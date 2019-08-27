# Web-servers benchmark

Benchmarking webservers built using different languages and libraries

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
  - version: 1.12.7
  - libs: 
    - net/nttp: 
nodejs:
  - version: 12.9.1
  - libs: 
    - express: ^4.17.1
r:
  - version: 3.6.1
  - libs:
    - plumber: 0.4.6
julia:
  - version: 1.1.1
  - libs:
    - Genie: 0.15.0
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

# Test

## Hello World!

## API json contract

The API response is expected as:

```json
{"data": "Hello World!"}
```

# Contribution

Feel free to add more benchmarks and open a pull request