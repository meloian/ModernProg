FROM ubuntu:latest

RUN apt-get update && apt-get install -y gcc make

WORKDIR /lab4

COPY src /lab4/src
COPY include /lab4/include
COPY tests /lab4/tests
COPY Makefile /lab4/

RUN make all

CMD ["./test"]
