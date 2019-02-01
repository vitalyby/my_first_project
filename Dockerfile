FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python3.5
COPY uspeh.py /tmp/
ENTRYPOINT ["python3.5", "/tmp/uspeh.py"]
