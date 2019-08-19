FROM gradle:4.10 AS build

COPY build.gradle .
COPY src ./src

RUN gradle clean build --no-daemon

FROM adoptopenjdk/openjdk8:jdk8u202-b08-alpine-slim AS serve

COPY --from=build /home/gradle/build/libs/gradle.jar /api.jar

CMD java -jar -Djava.security.egd=file:/dev/./urandom /api.jar
