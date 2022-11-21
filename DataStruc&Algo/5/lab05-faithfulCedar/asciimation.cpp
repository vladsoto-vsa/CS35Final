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

#include "adts/list.h"
#include "asciimationFunctions.h"
#include "linkedList.h"

using namespace std;

int main(int argc, char** argv) {
    if(argc != 2 && argc != 3) {
      cout << "Invalid number of command line arguments" << endl;
      return 1;
    }

    string filename;
    bool flag = false; // whether movie plays in normal or reverse

    if(argc == 2) {
      filename = argv[1];
    }
    else {
      string action = argv[1];

      if(action == "--reverse") {
        filename = argv[2];
        flag = true;
      }
      else {
        cout << "Invalid command line arguments" << endl;
        return 1;
      }    
    }

    List<pair<int, string>>* list = loadMovie(filename);
    
  
    if(flag == true) { 
      // if reverse flag is true, after file data becomes list through loadMovie, it is reversed
      List<pair<int, string>>* reverseList = new LinkedList<pair<int, string>>();
  
      while(list->getSize() > 0) {
        pair<int, string> p1 = list->removeLast();
        reverseList->insertLast(p1);  
      }

      delete list;
      list = reverseList;
    }

    playMovie(list);
    delete list;

    return 0;
}
