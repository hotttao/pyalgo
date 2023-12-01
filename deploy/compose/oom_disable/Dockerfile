FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install memtester
RUN apt-get install mbw
# RUN apt-get install -y python3.8
# RUN apt-get install -y python3-pip
COPY ./malloc.out .
RUN chmod +x ./malloc.out
# CMD ["memtester", "1024M"]
# CMD ["python3.8", "-c", "import time;a=bytes(1024*1024*5);time.sleep(1000000)"]
CMD ["./malloc.out", "52428800", "1000000"]