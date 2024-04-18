CC=gcc
CFLAGS=-Iinclude

all: main test

main: src/main.c src/account.c
	$(CC) $(CFLAGS) -o main src/main.c src/account.c

test: tests/test_account.c src/account.c
	$(CC) $(CFLAGS) -o test tests/test_account.c src/account.c

clean:
	rm -f main test 
