FROM golang:1.11-alpine AS build

WORKDIR /

COPY . .

RUN go build -o run_server api.go

FROM alpine:edge AS serve

COPY --from=build /run_server /
COPY --from=build /runner.sh /

CMD ./run_server