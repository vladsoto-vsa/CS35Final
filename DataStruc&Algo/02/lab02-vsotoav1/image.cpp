/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include "image.h"

#include <iostream>
using namespace std;

// Note: see image.h for documentation on functions.

int pixelToIndex(int width, int x, int y) {
    // TODO: implement this function correctly

    int index = 3*(width*y + x);

    return index; // this line is just filler so that the code compiles at first
}

void noRed(int width, int height, int* ppm) {
    // TODO: this image transformation
    for(int y = 0; y < height; y++){
      for(int x = 0; x < width; x++){
        int i = pixelToIndex(width, x, y);
        ppm[i] = 0;
    }
  } 
}
// TODO: write your other image transformation functions here
void noGreen(int width, int height, int* ppm) {
  for(int x = 0; x < width; x++){
    for(int y = 0; y < height; y++){
      int i = pixelToIndex(width, x, y);
      ppm[i+1] = 0;
    
    }
  }
}
void noBlue(int width, int height, int* ppm) {
  for(int x = 0; x < width; x++){
    for(int y = 0; y < height; y++){
      int i = pixelToIndex(width, x, y);
      ppm[i+2] = 0;
      
    }
  }
}    

void invert(int width, int height, int* ppm) {
  for(int x = 0; x < width; x++){
    for(int y = 0; y < height; y++){
      int i = pixelToIndex(width, x, y);
      ppm[i] = 255 - ppm[i];
      ppm[i+1] = 255 - ppm[i+1];
      ppm[i+2] = 255 - ppm[i+2];
    }
  }
}    

void grayscale(int width, int height, int* ppm) {
  for(int x = 0; x < width; x++){
    for(int y = 0; y < height; y++){
      int i = pixelToIndex(width, x, y);
      int avg = (ppm[i] + ppm[i+1] + ppm[i+2])/3;
      ppm[i] = avg;
      ppm[i+1] = avg;
      ppm[i+2] = avg;

    }
  }
}    

void flipHorizontally(int width, int height, int* ppm) {
  for(int x = 0; x < width/2; x++){
    for(int y = 0; y < height; y++){
      int i = pixelToIndex(width, x, y);
      int z = pixelToIndex(width, width-1-x, y);
      int red = ppm[i];
      int green = ppm[i+1];
      int blue = ppm[i+2];
      int twoRed= ppm[z];
      int twoGreen = ppm[z+1];
      int twoBlue = ppm[z+2];

      ppm[i] = twoRed;
      ppm[i+1] = twoGreen;
      ppm[i+2] = twoBlue;

      ppm[z] = red;
      ppm[z+1] = green;
      ppm[z+2] = blue;
    }
  }
}      
void flipVertically(int width, int height, int* ppm) {
  for(int x = 0; x < width; x++){
    for(int y = 0; y < height/2; y++){
      int i = pixelToIndex(width, x, y);
      int z = pixelToIndex(width, x, height-1-y);
      int red = ppm[i];
      int green = ppm[i+1];
      int blue = ppm[i+2];
      int twoRed= ppm[z];
      int twoGreen = ppm[z+1];
      int twoBlue = ppm[z+2];

      ppm[i] = twoRed;
      ppm[i+1] = twoGreen;
      ppm[i+2] = twoBlue;

      ppm[z] = red;
      ppm[z+1] = green;
      ppm[z+2] = blue;
    }
  }
}   


   
    
 /*Remember that the two flips are significantly harder than the
   other transofmations. We recommend that you work out the math
   on paper before attempting to write the code.
*/
