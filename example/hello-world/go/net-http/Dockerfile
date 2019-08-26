FROM golang:1.11-alpine AS build

WORKDIR /

COPY . .

RUN go build -o run_server api.go

FROM alpine:edge AS serve

COPY --from=build /run_server /
COPY --from=build /runner.sh /

RUN apk add wrk \
  && wget -O wrk_benchmark.sh https://raw.githubusercontent.com/kislerdm/web-server-benchmark/master/benchmark/wrk_benchmark.sh \
  && wget -O benchmark_summary.lua https://raw.githubusercontent.com/kislerdm/web-server-benchmark/master/benchmark/benchmark_summary.lua

CMD ./run_server