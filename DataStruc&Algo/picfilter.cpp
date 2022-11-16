/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <iostream>
#include <string>

#include "image.h"
#include "ppmio.h"

using namespace std;

int main(int argc, char** argv) {
    // TODO: write your program here
    // Remember:
    //   * The first command-line argument in argv is always the name of the
    //     program.
    //   * You can convert from char* to string just by assignment:
    //         string infile = argv[1];
    //   * You should (eventually) have code that deals with the case that your
    //     user gave you too few or too many command-line arguments.
    // Good luck!  Remember to ask for help!
    
    if (argc!=4) {
      cout << "incorrect command line!" << endl;
      return 1;
    }
    string picture = argv[1];
    string transformation = argv[2];
    string newPicture = argv[3];
    cout << "Filename: " << picture << endl;
  
    int width = ppm_width(picture);
    int height = ppm_height(picture);
    int* readPicture = read_ppm(picture);

    if (transformation == "noRed"){
       noRed(width, height, readPicture);
       write_ppm(newPicture, width, height, readPicture);
    }
    else if (transformation == "noGreen") {
      noGreen(width, height, readPicture);
        write_ppm(newPicture, width, height, readPicture);
    }
    else if (transformation == "noBlue") {
      noBlue(width, height, readPicture);
        write_ppm(newPicture, width, height, readPicture);
    }
    else if (transformation == "invert") {
      invert(width, height, readPicture);
        write_ppm(newPicture, width, height, readPicture);
    }
    else if (transformation == "grayscale") {
      grayscale(width, height, readPicture);
        write_ppm(newPicture, width, height, readPicture);
    }
    else if (transformation == "flipHorizontally") {
      flipHorizontally(width, height, readPicture);
        write_ppm(newPicture, width, height, readPicture);
    }
    else if (transformation == "flipVertically") {
      flipVertically(width, height, readPicture);
        write_ppm(newPicture, width, height, readPicture);
    }
    else {
      cout << "Transformation is invalid" << endl;
      delete[] readPicture;
      return 0;
    }

    delete[] readPicture;
    return 0;
}
