TARGETS=lab1 getaddrinfo

CFLAGS=-O0 -g -Wall -Wvla -Werror -Wno-error=unused-variable

all: $(TARGETS)

lab1: lab1.c
	gcc $(CFLAGS) -o lab1 lab1.c

getaddrinfo: getaddrinfo.c
	gcc $(CFLAGS) -o getaddrinfo getaddrinfo.c

clean:
	rm -f $(TARGETS)

