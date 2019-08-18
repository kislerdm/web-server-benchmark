FROM ubuntu:18.04 AS build

WORKDIR /app

# RUN apt-get update \
#   && apt-get install -y build-essential libboost-all-dev libtcmalloc-minimal4 git \
#   && ln -s /usr/lib/libtcmalloc_minimal.so.4 /usr/lib/libtcmalloc_minimal.so \
#   && git clone https://github.com/ipkn/crow.git ./crow_git \
#   && mv -f crow_git/include/* . \
#   && rm -fr crow_git

RUN apt-get update \
  && apt-get install -y build-essential libboost-all-dev libtcmalloc-minimal4 \
  && ln -s /usr/lib/libtcmalloc_minimal.so.4 /usr/lib/libtcmalloc_minimal.so

COPY . .

RUN g++ -o api -std=c++11 api.cc

FROM alpine:edge AS serve

COPY --from=build /app/api /api

CMD ./api
