/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include "rectangle.h"

// TODO: Define your Rectangle methods here.
Rectangle :: Rectangle(int x, int y, int width, int height, char symbol){
  this -> x = x;
  this -> y = y;
  this -> width = width;
  this -> height = height;
  this -> symbol = symbol;
}
void Rectangle :: draw(Grid* grid){
  for(int i = 0; i < width; i++){
    grid -> placeSymbol(x,y,symbol);
    int temp = y;
    for(int b = 0; b < height; b++){
      grid -> placeSymbol(x,y,symbol);
      y++;
    }
    y = temp;
    x++;
  }
}
 