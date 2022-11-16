/* Swarthmore College, CS 43, Lab 1
 * Copyright (c) 2022 Swarthmore College Computer Science Department,
 * Swarthmore PA
 * Professor Kevin Webb */


/*
This file currently contains a minimal TCP client example. The client connects
to port 8080 on the local machine and prints up to 255 received characters to
the console, then exits. To test it, try running a minimal server like this on
your local machine:
echo "Here is a message" | nc -l 8080
If you want to test without DNS, you can use the address 130.58.68.26 to reach
demo.cs.swarthmore.edu.
*/

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

int main(int argc, char** argv) {

    //Variables for later
    char *argvCopy, *hostname, *pathname, *fileName, *fileNameBackwards, *slashLocation = NULL;

    // Allocate memory for strings/arrays
    argvCopy = malloc(sizeof(char) * 1000000);
    if (argvCopy == NULL) {
        exit(0);
    }

    hostname = malloc(sizeof(char) * 1000000);
    if (hostname == NULL) {
        exit(0);
    }

    pathname = malloc(sizeof(char) * 1000000);
    if (pathname == NULL) {
        exit(0);
    }

    fileName = malloc(sizeof(char) * 1000000);
    if (fileName == NULL) {
        exit(0);
    }

    fileNameBackwards = malloc(sizeof(char) * 1000000);
    if (fileNameBackwards == NULL) {
        exit(0);
    }

    // Copy argv[1] over to argvCopy
    strcpy(argvCopy, argv[1]);

    // int array that holds indicies of '/' in our argv string
    int slashLocations[1000000];

    // Finding the first occurance of '/', appending it to slashLocations[]
    int counter = 0;
    slashLocation = strchr(argv[1], '/');
    slashLocations[counter] = slashLocation-argv[1]+1;

    // Loop over argv to fine all occurances of '/'
    // and append indicies to slashLocations[]
    while (slashLocation != NULL){
      counter += 1;
      slashLocation = strchr(slashLocation+1, '/');
      if(slashLocation == NULL){
        break;
      }
      slashLocations[counter] = slashLocation-argv[1]+1;
    }


    // Loop over argvCopy from 2nd to 3rd '/'
    // and append it to hostname[]
    int hostCounter = 0;
    for(int i = slashLocations[1]; i < slashLocations[2]-1; i++){
      hostname[hostCounter] = argvCopy[i];
      hostCounter += 1;
    }
    printf("this is hostname: %s\n", hostname);


    // Loop over argvCopy from 3rd '/' to end
    // and append it to pathname[]
    int pathCounter = 0;
    for(int j = slashLocations[2]-1; j < strlen(argvCopy); j++){
      pathname[pathCounter] = argvCopy[j];
      pathCounter += 1;
    }
    printf("this is pathname: %s\n", pathname);


    // Loop over argvCopy from end to first '/'
    // and append it to fileNameBackwards[]
    int fileNameBackwardsCounter = 0;
    for(int k = strlen(argvCopy)-1; k > 0; k--){
      if(argvCopy[k] != '/'){
        fileNameBackwards[fileNameBackwardsCounter] = argvCopy[k];
        fileNameBackwardsCounter += 1;
      }
      else{
        break;
      }
    }


    // Loop over fileNameBackwards
    // and append it to fileName[]
    int fileNameCounter = 0;
    for (int l = strlen(fileNameBackwards)-1; l >= 0; l--){
      fileName[fileNameCounter] = fileNameBackwards[l];
      fileNameCounter += 1;
    }
    printf("this is fileName: %s\n", fileName);

    /* Create a TCP socket (SOCK_STREAM). */
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("socket");
        exit(1);
    }

    struct addrinfo *result = NULL;

    /* Call getaddrinfo.  The first parameter is the hostname to resolve
     * (string).  The next two can safely be NULL (they allow setting options
     * we don't need).  The final parameter should be the address of struct
     * addrinfo pointer to be used as described above. */
    if (getaddrinfo(hostname, NULL, NULL, &result)) {
        printf("getaddrinfo failed");
        exit(1);
    }

    /* This structure represents an address that you can associate with a
     * socket.  It's of type "sockaddr_in" because this is a socket for use on
     * the Internet.  It stores a family (socket type AF_INET for Internet), an
     * IP address to identify a host, and a port number to identify an
     * application (details later in semester). */
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr = ((struct sockaddr_in*)result->ai_addr)->sin_addr;
    addr.sin_port = htons(80); /* byte order is significant (details later) */

    /* Initiate a connection to the server. */
    int res = connect(sock, (struct sockaddr*)&addr, sizeof(addr));
    if (res < 0) {
        perror("connect");
        exit(1);
    }


    char *HTTPrequest = NULL;
    HTTPrequest = malloc(sizeof(char) * 1000000);
    if (HTTPrequest == NULL) {
        exit(0);
    }

    sprintf(HTTPrequest, "GET %s HTTP/1.0\r\n"
                      "Host: %s\r\n"
                      "\r\n", pathname, hostname);
    printf("%s", HTTPrequest);


    // send request

    int sent, totalSent = 0;
    int length = strlen(HTTPrequest);
    int totalLengthRequest = length;
    do{
      sent = send(sock,HTTPrequest+totalSent,length-totalSent,0);
      if (sent < 0){
        perror("ERROR");
      }
      totalSent += sent;
    }while(totalSent < totalLengthRequest);

    //receive request
    int rec, totalRec = 0;
    char *contents = NULL;
    contents = malloc(sizeof(char) * 1000000);
    if (contents == NULL) {
        exit(0);
    }
    do{
      rec = recv(sock, contents+totalRec, 1000000-totalRec, 0);
      if (rec < 0){
        perror("ERROR");
      }
      totalRec += rec;
    }while(rec != 0);

    //create the body of the request
    char *body = NULL;
    body = strstr(contents, "\r\n\r\n");
    body = body + 4;


    // save request to file
    FILE *file;

    file = fopen(fileName, "w");
    if(file == NULL){
      printf("Unable to create file.\n");
      exit(0);
    }

    // close the file
    if (fclose(file)) {
      perror("fclose file");
      exit(1);
    }

    /* Close the socket/connection now that we're done with it. */
    if (close(sock)) {
        perror("close sock");
        exit(1);
    }

    free(argvCopy);
    free(hostname);
    free(pathname);
    free(fileName);
    free(fileNameBackwards);
    free(HTTPrequest);
    free(contents);
    free(result);

    /* Indicates successful program termination. */
    return 0;
}
