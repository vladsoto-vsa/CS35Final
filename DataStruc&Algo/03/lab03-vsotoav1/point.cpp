/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include "point.h"

// TODO: Define your Point methods here.
Point :: Point(int x, int y, char symbol){
  this -> x = x;
  this -> y = y;
  this -> symbol = symbol;
}
void Point :: draw(Grid* grid){
 grid -> placeSymbol(x,y,symbol); 
}
