void processRequest(int sock){

  // if path does not exist
  if(pathTypeInt !=  0){
    throwError(sock);
  }
  // path exists
  int pathTypeDirectory = S_ISDIR(pathType.st_mode);
  // path is a directory, it could have a file
  if(pathTypeDirectory != 0){
    PATH_IS_A_DIRECTORY_MIGHT_CONTAIN_FILE_THOUGH
    if(variable = fopen(path+index.html)){
      fclose()
      DIRECTORY_CONTAINS_INDEX_DOT_HTML
    }
    else{
      PATH_IS_NORMAL_DIRECTORY
    }
  }
  // path is a file
  else{
    PATH_IS_A_FILE
  }
}


      printf("stat() returned 0, no stat() error\n");
      printf("this is requestedPath: *%s*\n", requestedPath);

      // if response is directory, do the following
      int pathTypeDirectory = S_ISDIR(pathType.st_mode);
      if(pathTypeDirectory != 0){
          printf("pathType is a directory\n");

          // try to open a file called 'index.html'
          // or whatever requestedPath is called at this point
          // char freadBuffer[4096];
          char *requestedPathPlusIndex = NULL;
          requestedPathPlusIndex = malloc(sizeof(char*)*(4000));
          if(requestedPathPlusIndex == NULL){
            exit(0);
          }
          strcpy(requestedPathPlusIndex, requestedPath);
          strcat(requestedPathPlusIndex, "/index.html");
          printf("this is requestedPathPlusIndex: *%s*\n", requestedPathPlusIndex);
          file = fopen(requestedPathPlusIndex, "r");
          if(file){
            fclose(file);
            printf("found/read a file called '%s'\n", requestedPathPlusIndex);
            printf("I will return it to you now!\n");
            makeResponse(requestedPathPlusIndex, sock);
          }

          // there is not a 'file' called that
          // then print error
          else{
            printf("Unable to read/find a file '%s' in this directory!!\n", requestedPathPlusIndex);
            printf("I should respond with the directory listing now!!\n");
            // processDirectory(sock, requestedPath, length);
          }
      }
      // if response is a file
      else{
          // char freadBuffer[4096];
          // file = fopen("index.html", "r");
          // length = fread(freadBuffer, 1, 4096, file);
          // printf("this is length: *%ld*\n", length);
          printf("requestedPath is not a directory\n");
          printf("Need to send a file called *%s* now!\n", requestedPath);
          makeResponse(requestedPath, sock);
          // processFile(sock, requestedPath, length);
      }
 }
  close(sock);
}
