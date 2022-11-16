/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <iostream>
#include <stdexcept>

#include "picture.h"

using namespace std;

Picture::Picture() {
    // TODO: implement Picture::Picture
    this -> numberOfShapes = 0;
    this -> shapes = new Shape*[50];
}

Picture::~Picture() {
    // TODO: implement Picture::~Picture
    for (int i=0;i<50;i++){
        delete shapes[i];
    }
    delete[] shapes;
}

string Picture::toString() {
    // TODO: implement Picture::toString
    Grid* newGrid = new Grid();
    for(int i=0; i<numberOfShapes; i++){
        shapes[i] -> draw(newGrid);
    }

    return newGrid -> toString();
}

void Picture::print() {
    cout << this->toString() << endl;
}

void Picture::addShape(Shape* shape) {
    // TODO: implement Picture::addShape
    int index = numberOfShapes;
    shapes[index] = shape;
    numberOfShapes++;
}
delete[] newGrid;
