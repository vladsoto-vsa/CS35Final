/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <string>
#include <iostream>

#include <algorithm>
#include <random>
#include <stdexcept>
#include <string>
#include <vector>

#include <UnitTest++/UnitTest++.h>

#include "adts/dictionary.h"
#include "hashFunctions.h"
#include "hashTable.h"

using namespace std;

int main(int argc, char** argv) {
    // You can use this main to experiment with the code you have written
    Dictionary<int, string>* dictionary = new HashTable<int, string>();
    cout << dictionary->getSize() << endl;
    dictionary->insert(0, "three");
    dictionary->insert(0, "five");
    cout << dictionary->getSize() << endl;
    cout << dictionary->get(0) << endl;
    delete dictionary;
    return 0;
}
