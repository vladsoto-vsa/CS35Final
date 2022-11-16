#include <arpa/inet.h>
#include <netdb.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/select.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

/* This is a complete example that shows how to resolve a hostname to
 * an IP address using the domain name system (DNS).
 *
 * You should use this function (getaddrinfo) in your lab code. */

int main(int argc, char** argv) {
    /* Ensure hostname arg is given. */
    if(argc != 2) {
        printf("Usage: %s <hostname>\n", argv[0]);
        exit(1);
    }

    /* Declare a struct pointer for the name resolution results.
     * You'll pass in the address of this pointer to getaddrinfo,
     * and it will:
     *   * On failure, set this pointer to NULL.
     *   * On success, allocate memory and fill in this pointer
     *     to refer to the memory.  The contents of the struct
     *     it points to will contain the resolved IP address. */
    struct addrinfo *result = NULL;

    /* Call getaddrinfo.  The first parameter is the hostname to resolve
     * (string).  The next two can safely be NULL (they allow setting options
     * we don't need).  The final parameter should be the address of struct
     * addrinfo pointer to be used as described above. */
    if (getaddrinfo(argv[1], NULL, NULL, &result)) {
        printf("getaddrinfo failed");
        exit(1);
    }

    /* ALWAYS check the result of any function that can fail! Don't attempt to
     * use the result if it's NULL. */
    if(result != NULL) {
        printf("The name %s resolves to IP address %s\n",
                argv[1],inet_ntoa(((struct sockaddr_in*)result->ai_addr)->sin_addr));
    } else {
        printf("getaddrinfo failed");
        exit(1);
    }

    /* On success, the getaddrinfo function allocates memory. This function
     * frees that memory for you, after you no longer need it. */
    freeaddrinfo(result);

    return 0;
}


/* Note: you can copy the IP address to your sockaddr struct like this:

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr = ((struct sockaddr_in*)result->ai_addr)->sin_addr;
    addr.sin_port = ...
    ...

You can safely free the struct with freeaddrinfo after performing this copy.
*/
