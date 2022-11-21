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
#include <utility>

#include "maze.h"
#include "mazeUtils.h"

using namespace std;

int main(int argc, char** argv) {
    if(argc != 3) {
      cout << "Invalid number of command line arguments" << endl;
      return 0;
    }
    
    string filename = argv[1];
    string searchType = argv[2]; // breadth or depth search
    Maze* map; 
    List<Position*>* path;

    try {
        map = loadMap(filename); 
    } catch (runtime_error e) {
        cout << "Map failed to load" << endl;
        return 0;
    }

    if(searchType == "depth") {
      path = map->solveDepthFirst();
    } 
    else if(searchType == "breadth") {
      path = map->solveBreadthFirst();
    }
    else {
      cout << "Invalid command line argument" << endl;
      return 0;
    }   

    if(path != nullptr) {
      cout << renderAnswer(map, path) << endl;
    }
    else {
      cout << filename << " has no solution" << endl;
    }

    delete map;
    delete path;

    return 0;
}
