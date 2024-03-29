FROM openjdk:latest

ENV minRAM=750
ENV maxRAM=1024

RUN mkdir server

COPY content/* /server 
WORKDIR /server 


ENTRYPOINT java -Xmx${maxRAM}M -Xms${minRAM}M -jar server.jar nogui

EXPOSE 25565