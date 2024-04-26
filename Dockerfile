FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY lab4/include /app/lab4/include
COPY lab4/src /app/lab4/src
COPY lab4/tests /app/lab4/tests
COPY lab4/Makefile /app/lab4/

COPY lab1 /app/lab1
COPY lab2 /app/lab2
COPY lab3 /app/lab3

COPY .github /app/.github

COPY .gitignore /app/

RUN cd /app/lab4 && make all

ENV NAME World

CMD ["python3", "-m", "unittest", "discover", "-s", "/app/lab1", "-p", "test_*.py"] 