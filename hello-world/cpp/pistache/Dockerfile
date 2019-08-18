FROM ubuntu:18.04 AS build

# RUN apk update && apk add g++ git cmake make
RUN deb http://ppa.launchpad.net/kip/pistache-unstable/ubuntu disco main \
  && apt-get update \
  && apt-get install -y software-properties-common 

RUN add-apt-repository ppa:kip/pistache \
  && apt-get install -y libpistache-dev

WORKDIR /app

# RUN git clone https://github.com/oktal/pistache.git \
#   && cd pistache \
#   && git submodule update --init \
#   && mkdir build \
#   && cd build \
#   && cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release \
#   -DPISTACHE_BUILD_EXAMPLES=false \
#   -DPISTACHE_BUILD_TESTS=false \
#   -DPISTACHE_BUILD_DOCS=false \
#   -DPISTACHE_USE_SSL=false \
#   ../ \
#   && make -j4 \
#   && make install

COPY . .

RUN g++ api.cc

FROM alpine:edge AS serve

COPY --from=build /app/api /api

CMD ./api
