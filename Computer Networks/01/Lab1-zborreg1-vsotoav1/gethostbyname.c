#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <arpa/inet.h>

/* DON'T USE THIS.  This function is old and needs to go away.  I'm putting
 * this here as an example so that you can see it.  Lots of code out there
 * today still uses it, but it shouldn't be used in anything new. */

void usage(char *invoked_as) {
    printf("Usage: %s <hostname>\n", invoked_as);
    exit(1);
}

int main(int argc, char** argv)
{
    if (argc < 2) {
        usage(argv[0]);
    }

    struct hostent *result;
    result = gethostbyname(argv[1]);
    if (result != NULL) {

        /* The third argument to printf looks a little complicated.
             inet_ntoa takes a 'struct in_addr' and produces a string 
             containing the IP address written out in plaintext.

             But what's with all the casting? The h_addr_list contains
             a list of IP addresses, each address 4 bytes long, but in
             true C style, it's untyped: just a char array. On the
             other hand, a 'struct in_addr' is just 4 bytes too. So
             we first cast the char* to the first address as a 
             'struct in_addr *', and then de-reference the pointer. 
             In the end we have the required 'struct in_addr', passed
             to inet_ntoa.

             A longer (and some would argue, better) way to write it:
             char *rawaddr = result->h_addr_list[0]; // points to 4 byte address
             struct in_addr *addr = (struct in_addr*)rawaddr; // cast to correct type
             char *straddr = inet_ntoa(*addr); // pass the dereferenced value to ntoa
        */

        printf("The name %s resolves to IP address %s\n",
                     argv[1],inet_ntoa(*((struct in_addr*)result->h_addr_list[0])));
    } else {
        herror("An error occurred during host name lookup\n");
        exit(1);
    }

    return 0;
}
