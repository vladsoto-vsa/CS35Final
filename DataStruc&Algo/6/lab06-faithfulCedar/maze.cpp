/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <stdexcept>

/* ADTs */
#include "adts/list.h"
#include "adts/orderedCollection.h"
#include "adts/queue.h"
#include "adts/stack.h"

/* Implementations of above ADTs */
#include "adts/stlList.h"
#include "linkedQueue.h"
#include "linkedStack.h"

#include "maze.h"

using namespace std;

Maze::Maze(int width, int height) {
    this->width = width;
    this->height = height;

    this->positions = new Position**[this->width];

    for(int i = 0; i < this->width; i++) {
        this->positions[i] = new Position*[this->height];
        
        for(int j = 0; j < this->height; j++) {
            this->positions[i][j] = new Position(i, j);
        }
    }
}

Maze::~Maze() {
    for(int i = 0; i < width; i++) {
        for(int j = 0; j < height; j++) {
            delete positions[i][j]; 
        }
        delete[] positions[i];
    }
    delete[] positions;
}

int Maze::getWidth() {
    return this->width;
}

int Maze::getHeight() {
    return this->height;
}

bool Maze::isWall(int x, int y) { 
    return this->positions[x][y]->isWall();
}

void Maze::setWall(int x, int y) {
    this->positions[x][y]->setWall();   
}

List<Position*>* Maze::solveBreadthFirst() {
    LinkedQueue<Position*>* list = new LinkedQueue<Position*>();
    List<Position*>* path = solve(list);
    delete list;
    return path;
}

List<Position*>* Maze::solveDepthFirst() {
    LinkedStack<Position*>* list = new LinkedStack<Position*>();
    List<Position*>* path = solve(list);
    delete list; 
    return path;
}

List<Position*>* Maze::solve(OrderedCollection<Position*>* exploration) {
    this->positions[0][0]->setVisited();
    exploration->insert(this->positions[0][0]);
    Position* current; 

    while(exploration->getSize() > 0) {
        current = exploration->remove();
        
        if(current->getX() == this->width-1 && current->getY() == this->height-1) {
            // if the current position is the bottom right corner
            List<Position*>* path = new STLList<Position*>();

            path->insertFirst(current);
            while(current->getPrevious() != nullptr) {
                current = current->getPrevious();
                path->insertFirst(current);
            }
    
            return path;
        }
           
        List<Position*>* neighbors = getNeighbors(current); // list containing valid neighbors of current position
        int size = neighbors->getSize();
        
        for(int i = 0; i < size; i++) {
            if(!neighbors->getFirst()->isVisited()) {
                exploration->insert(neighbors->getFirst());
                neighbors->getFirst()->setVisited();
                neighbors->getFirst()->setPrevious(current);
            }   
            neighbors->removeFirst();
        }
        delete neighbors;
    }      

    return nullptr;
    // if the maze is unsolvable 
}

List<Position*>* Maze::getNeighbors(Position* position) {
    int x = position->getX();
    int y = position->getY();
    List<Position*>* neighbors = new STLList<Position*>();

    if(y+1 < this->height && !this->positions[x][y+1]->isWall()) {
        neighbors->insertFirst(this->positions[x][y+1]);
    }

    if(x-1 >= 0 && !this->positions[x-1][y]->isWall()){
        neighbors->insertFirst(this->positions[x-1][y]);
    }

    if(x+1 < this->width && !this->positions[x+1][y]->isWall()) {
        neighbors->insertFirst(positions[x+1][y]);
    }

    if(y-1 >= 0 && !this->positions[x][y-1]->isWall()) {
        neighbors->insertFirst(this->positions[x][y-1]);   
    }

    return neighbors;
}
