#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/* The function that each new thread will execute when it begins. To make this
 * generic, it returns a (void *) and takes a (void *) as it's argument.  In C,
 * (void *) is essentially a typeless pointer to anything that you can cast to
 * anything else when necessary. For example, look at the argument to this
 * thread function.  Its type is (void *), but since we KNOW that the type of
 * the argument is really a (int *), the first thing we do is cast
 * it to that type, to make it usable. */
void *thread_function(void *argument_value) {
    int *argument = (int *) argument_value;
    int id = *argument;

    /* Free the memory that was allocated to store our thread argument on line
     * number 43. We already copied its value to the 'id' integer, so we can
     * use 'id' to reference this number going forward.*/
    free(argument);

    printf("Hi, I'm thread number %d\n", id);

    return NULL;
}

int main(int argc, char **argv) {
    int num_threads, i;

    if (argc < 2) {
        printf("I require an argument - the number of threads to create.\n");
        exit(1);
    }

    num_threads = atoi(argv[1]);

    for (i = 0; i < num_threads; i++) {
        pthread_t new_thread;

        /* A place to store our thread's argument.  In this case, a pointer to
         * a single integer value, the thread number (loop iteration). */
        int *argument = malloc(sizeof(int));
        *argument = i;

        /* Create thread #i.  We give it a pointer to the thread structure that
         * it will use to store thread state (&new_thread), attributes (NULL,
         * for defaults), a pointer to the function to execute
         * (thread_function), and the argument to that thread function.  The
         * argument can be a pointer to anything that isn't on the stack, since
         * the thread will get its own stack when it starts up. */
        int retval = pthread_create(&new_thread, NULL, thread_function, argument);
        if (retval) {
            printf("pthread_create() failed\n");
            exit(1);
        }

        /* "Detach" the thread.  This makes it automatically clean up after
         * itself when it terminates, so that you never need to call
         * pthread_join() on it. */
        retval = pthread_detach(new_thread);
        if (retval) {
            printf("pthread_detach() failed\n");
            exit(1);
        }
    }

    /* Give the threads a chance to do their thing before we terminate. */
    usleep(500000);

    return 0;
}
