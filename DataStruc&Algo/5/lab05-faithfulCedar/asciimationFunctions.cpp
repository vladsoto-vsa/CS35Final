/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unistd.h>
#include <utility>

#include "adts/list.h"
#include "asciimationFunctions.h"
#include "linkedList.h"

using namespace std;


List<pair<int, string>>* loadMovie(string filename) {
    ifstream myFile;
    string data;
    int duration;
    List<pair<int, string>>* list = new LinkedList<pair<int, string>>();

    myFile.open(filename);
    if(!myFile.is_open()) {
     throw runtime_error("file " + filename + "failed to open ");
    }

    getline(myFile, data);

    while (!myFile.eof()) {
        string frame_contents; 
        duration = stoi(data); // converts string duration to int

        for(int i = 0; i < 13; i++) {
            // adds 13 lines of movie frame strings
            getline(myFile, data);
            frame_contents += data;
            frame_contents += "\n";
        }

        pair<int, string> p1(duration, frame_contents);
        list->insertLast(p1);
        
        getline(myFile, data);
    }
    return list;
}

void playMovie(List<pair<int, string>>* list) {
    for(int i = 0; i < list->getSize(); i++) {
        cout << list->get(i).second << endl; 
        usleep((1000000/15)*list->get(i).first); // duration for how long frame lasts
        system("clear");
    }
}