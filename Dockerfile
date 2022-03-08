FROM eclipse-temurin:17-jdk

EXPOSE 25565 25575

RUN apt-get update -y

RUN apt-get install git python3 -y

VOLUME ["/data"]
WORKDIR /data

COPY scripts/* .