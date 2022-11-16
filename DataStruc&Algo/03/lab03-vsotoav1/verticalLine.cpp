/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include "verticalLine.h"

// TODO: Define your VerticalLine methods here.
VerticalLine :: VerticalLine(int x, int y, int length, char symbol){
  this -> x = x;
  this -> y = y;
  this -> length = length;
  this -> symbol = symbol;
}
void VerticalLine :: draw(Grid* grid){
  for(int i = 0; i < length; i++){
    grid -> placeSymbol(x,y,symbol);
    y++;
  }
}


 