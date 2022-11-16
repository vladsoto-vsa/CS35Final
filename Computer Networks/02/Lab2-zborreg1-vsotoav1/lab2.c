/* Swarthmore College, CS 43, Lab 2
 * Copyright (c) 2022 Swarthmore College Computer Science Department,
 * Swarthmore PA
 * Professor Kevin Webb */

#include <errno.h>
#include <netinet/in.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/select.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <dirent.h>

#define BACKLOG (10)

void sendData(int socket, char *dataToSend, int length){
  int sent, totalSent = 0;

  do{
    sent = send(socket,dataToSend+totalSent,length-totalSent,0);
    if (sent < 0){
      perror("ERROR");
      exit(1);
    }
    totalSent += sent;
  }while(totalSent < length);
}

void throwError(int socket){
  char *errorMessage = NULL;
  int lengthError;
  errorMessage = malloc(sizeof(char*) * (4000));
  if(errorMessage == NULL){
    perror("bruh!");
    exit(1);
  }
  sprintf(errorMessage, "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n <!DOCTYPE html><html><body><h1>Bruh!!</h1><p>you messed up man. Oh and 404 page not found too.</p></body></html>");
  lengthError = strlen(errorMessage);
  sendData(socket, errorMessage, lengthError);
  // free(errorMessage);
  exit(1);
}

void sendDirectory(char *requestedPath, int sock){
  DIR *directory;
  struct dirent *dir;

  directory = opendir(requestedPath);
  char response[4096];
  sprintf(response, "HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n");
  strcat(response, "<html><body><ul>");

  if(directory == NULL){
    perror("Directory cannot be opened!");
    exit(1);
  }
  else{
    while((dir = readdir(directory)) != NULL){
      strcat(response, "<li><a href=\"");
      strcat(response, dir->d_name);
      if(dir->d_type == DT_DIR){
        strcat(response, "/");
      }
      strcat(response, "\">");
      strcat(response, dir->d_name);
      if(dir->d_type == DT_DIR){
        strcat(response, "/");
      }
      strcat(response, "</a></li>");
    }
    strcat(response, "</ul></body></html>");
    sendData(sock, response, strlen(response));
  }
}

void generateHeader(char *fileEnding, char *header, char *requestedPath){
  char *contentType;
  char *html = ".html";
  char *txt = ".txt";
  char *jpeg = ".jpeg";
  char *jpg = ".jpg";
  char *gif = ".gif";
  char *png = ".png";
  char *pdf = ".pdf";
  char *ico = ".ico";

  if(strcmp(fileEnding, html) == 0){
    contentType = "text/html";
  }
  else if(strcmp(fileEnding, txt) == 0){
    contentType = "text/plain";
  }
  else if(strcmp(fileEnding, jpeg) == 0){
    contentType = "image/jpeg";
  }
  else if(strcmp(fileEnding, jpg) == 0){
    contentType = "image/jpg";
  }
  else if(strcmp(fileEnding, gif) == 0){
    contentType = "image/gif";
  }
  else if(strcmp(fileEnding, png) == 0){
    contentType = "image/png";
  }
  else if(strcmp(fileEnding, pdf) == 0){
    contentType = "application/pdf";
  }
  else if(strcmp(fileEnding, ico) == 0){
    contentType = "image/x-icon";
  }
  else{
    printf("ERROR, no matching file endings!\n");
    printf("Exiting now...\n");
    exit(0);
  }
  sprintf(header, "HTTP/1.0 200 OK\r\nContent-Type: %s\r\n\r\n", contentType);
}

void sendFile(char *requestedPath, int socket){
  char* fileEnding, *header;
  int read, headerLen;
  const char dot = '.';
  char freadBuffer[4096];
  FILE *file;

  fileEnding = malloc(sizeof(char*) * (4000));
  header = malloc(sizeof(char*) * (4000));
  fileEnding = strchr(requestedPath, dot);
  generateHeader(fileEnding, header, requestedPath);

  file = fopen(requestedPath, "r");
  if((file = fopen(requestedPath, "r")) == NULL){
    exit(1);
  }

  headerLen = strlen(header);
  sendData(socket, header, headerLen);

  while((read = fread(freadBuffer, 1, sizeof(freadBuffer), file)) != 0){
    sendData(socket, freadBuffer, read);
  }

  // free(fileEnding);
  // free(header);
}

void processRequest(int sock){
  // Create variables for later
  int rec, totalRec = 0;
  int size = 4000;
  char *buffer, *pathname, *contentType = NULL;
  buffer = malloc(sizeof(char*) * (4000));
  pathname = malloc(sizeof(char*) * (4000));
  contentType = malloc(sizeof(char*) * (4000));
  const char ch = '/';
  const char space = ' ';

  // Check if arrays were created
  if(buffer == NULL){
    exit(0);
  }
  if(pathname == NULL){
    exit(0);
  }
  if(contentType == NULL){
    exit(0);
  }

  // Keep receiving buffer and stop when pathname is no longer NULL
  do{
    rec = recv(sock, buffer+totalRec, size-totalRec, 0);
    if (rec < 0){
      perror("ERROR");
      exit(1);
    }
    if (rec == 0){
      break;
    }
    totalRec += rec;
    pathname = strstr(buffer, "\r\n\r\n");
  }while(pathname == NULL);

  // Create variables for later
  char *pathRaw = strchr(buffer, ch);
  char *requestedPath = NULL;
  // Check if requestedPath was created
  //requestedPath = malloc(sizeof(char*)*(4000));
  /*
  if(requestedPath == NULL){
    exit(0);
  }
  */
  char requestedPathArray[4096];
  memset(requestedPathArray, 0, sizeof(requestedPathArray[0]));     //did something here using memset


  // Extract the requested path
  int i = 0;
  while(pathRaw[i] != space){
    requestedPath[i] = pathRaw[i];
    i++;
  }
  requestedPath = requestedPath + 1;

  struct stat pathType;
  // FILE *file;
  int pathTypeInt = stat(requestedPath, &pathType);
  char requestedPathPlusIndex[4096];
  strcpy(requestedPathPlusIndex, requestedPath);
  strcat(requestedPathPlusIndex, "index.html");


  // if path does not exist
  if(pathTypeInt !=  0){
    throwError(sock);
  }
  // path exists
  int pathTypeDirectory = S_ISDIR(pathType.st_mode);
  // path is a directory, it could have a file
  if(pathTypeDirectory != 0){
    int hasIndex = stat(requestedPathPlusIndex, &pathType);
    if(hasIndex == 0){
      sendFile(requestedPathPlusIndex, sock);
    }
    else{
      sendDirectory(requestedPath, sock);
    }
  }
  else{
    sendFile(requestedPath, sock);
  }
  close(sock);
  // free(buffer);
  // free(pathname);
  // free(contentType);
  // free(requestedPath);
}

void *thread_function(void *sock){
  int *argument = (int *) sock;
  int id = *argument;

  processRequest(id);

  free(argument);
  return NULL;
}

int main(int argc, char **argv) {
  /* For checking return values. */
  int retval;

  /* To store the user-specified port. */
  int port;

  /* The socket to bind/listen/accept on. */
  int server_sock;

  /* A flag to pass to turn on the SO_REUSEADDR option. */
  int reuse_true;

  /* Make sure we get the right number of arguments. */
  if (argc != 3) {
    printf("Usage: %s <port> <document root>\n", argv[0]);
    exit(1);
  }

  /* Read the port number from the first command line argument. */
  port = atoi(argv[1]);

  printf("Webserver configuration:\n");
  printf("\tPort: %d\n", port);
  printf("\tDocument root: %s\n", argv[2]);  //argv[2] is document root

  int docRoot = chdir(argv[2]);

  if (docRoot != 0){
    perror("docRoot error");
    exit(0);
  }

  /* Create a socket to which clients will connect. */
  server_sock = socket(AF_INET, SOCK_STREAM, 0);
  if (server_sock < 0) {
    perror("Creating socket failed");
    exit(1);
  }

  /* A server socket is bound to a port, which it will listen on for incoming
  * connections.  By default, when a bound socket is closed, the OS waits a
  * couple of minutes before allowing the port to be re-used.  This is
  * inconvenient when you're developing an application, since it means that
  * you have to wait a minute or two after you run to try things again, so
  * we can disable the wait time by setting a socket option called
  * SO_REUSEADDR, which tells the OS that we want to be able to immediately
  * re-bind to that same port. See the socket(7) man page ("man 7 socket")
  * and setsockopt(2) pages for more details about socket options. */
  reuse_true = 1;
  retval = setsockopt(server_sock, SOL_SOCKET, SO_REUSEADDR, &reuse_true,
      sizeof(reuse_true));
  if (retval < 0) {
    perror("Setting socket option failed");
    exit(1);
  }

  /* Create an address structure.  This is very similar to what we saw on the
  * client side, only this time, we're not telling the OS where to connect,
  * we're telling it to bind to a particular address and port to receive
  * incoming connections.  Like the client side, we must use htons() to put
  * the port number in network byte order.  When specifying the IP address,
  * we use a special constant, INADDR_ANY, which tells the OS to bind to all
  * of the system's addresses.  If your machine has multiple network
  * interfaces, and you only wanted to accept connections from one of them,
  * you could supply the address of the interface you wanted to use here. */
  struct sockaddr_in addr;
  addr.sin_family = AF_INET;
  addr.sin_port = htons(port);
  addr.sin_addr.s_addr = INADDR_ANY;

  /* TODO: call bind.  As its name implies, this system call asks the OS to
  * bind the socket to the address and port specified above. Be sure to
  * check for errors.  On failure, call perror("bind") to get a
  * human-readable description of the error and then terminate. You can cast
  * the address of the "addr" struct defined above to a (struct sockaddr *)
  * when passing it to bind. */
  int bindVal;

  bindVal = bind(server_sock, (struct sockaddr*)&addr, sizeof(addr));

  if (bindVal  != 0){
    perror("bindVal error");
    exit(0);
  }

  /* TODO: call listen. Now that we've bound to an address and port, we tell
  * the OS that we're ready to start listening for client connections.  This
  * effectively activates the server socket.  BACKLOG (#defined above) tells
  * the OS how much space to reserve for incoming connections that have not
  * yet been accepted. Similar to bind, check for errors and call
  * perror("listen") for human-readable details. */
  int listenVal;
  listenVal = listen(server_sock,BACKLOG);

  if (listenVal  != 0){
    perror("listenVal error");
    exit(0);
  }

  int counter = 0;
  while (1) {
  counter += 1;
  /* Declare a socket for the client connection. */
  int sock;

  /* Another address structure.  This time, the system will automatically
  * fill it in, when we accept a connection, to tell us where the
  * connection came from. */
  struct sockaddr_in remote_addr;
  unsigned int socklen = sizeof(struct sockaddr_in);

  /* Accept the first waiting connection from the server socket and
  * populate the address information.  The result (sock) is a socket
  * descriptor for the conversation with the newly connected client.  If
  * there are no pending connections in the back log, this function will
  * block indefinitely while waiting for a client connection to be made.
  * */

  sock = accept(server_sock, (struct sockaddr *) &remote_addr, &socklen);

  if (sock >= 0) {
    max_fd = max_fd + 1;
    exit(1);
  }

  // probably where we need to put the threads
  pthread_t new_thread;
  int *argument = malloc(sizeof(int)); //cannot malloc this
  *argument = sock;
  int retval = pthread_create(&new_thread, NULL, thread_function, argument);
  if (retval) {
      printf("pthread_create() failed\n");
      exit(1);
  }

  retval = pthread_detach(new_thread);
  if (retval) {
      printf("pthread_detach() failed\n");
      exit(1);
  }

  usleep(500000);

  // processRequest(sock);

  }
  close(server_sock);
}
