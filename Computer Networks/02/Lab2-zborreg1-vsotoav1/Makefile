TARGETS=lab2 thread_detach_example

CFLAGS=-O0 -g -Wall -Wvla -Werror -Wno-error=unused-variable -Wno-error=unused-but-set-variable

all: $(TARGETS)

lab2: lab2.c
	gcc $(CFLAGS) -o lab2 lab2.c -lpthread

thread_detach_example: thread_detach_example.c
	gcc $(CFLAGS) -o thread_detach_example thread_detach_example.c -lpthread

clean:
	rm -f $(TARGETS)
