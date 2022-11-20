/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <UnitTest++/UnitTest++.h>
#include <iostream>

#include "mergeSort.h"

using namespace std;

TEST(threeElements) {
  // Create a static array containing the numbers 4, 8, 6.
  int array[3] = {4, 8, 6};
  mergeSort(array, 3);
  CHECK_EQUAL(4, array[0]);
  CHECK_EQUAL(6, array[1]);
  CHECK_EQUAL(8, array[2]);
}

TEST(reverseSorted) {
  int size = 20;
  // Create a dynamically-allocated array
  int *array = new int[size];
  for (int i = 0; i < size; i++) {
    array[i] = size - 1 - i;
  }
  mergeSort(array, size);
  for (int i = 0; i < size; i++) {
    CHECK_EQUAL(i, array[i]);
  }
  // de-allocate array
  delete[] array;
  array = nullptr;
}

TEST(singleArray){
  //creates a single element static array containing the value 5
  int array[1] = {5};
  mergeSort(array, 1);
  CHECK_EQUAL(5, array[0]);
}

TEST(orderedArray){
  //creates a static array with elements already ordered
  int array[6] = {1, 2, 3, 4, 5, 6};
  mergeSort(array, 6);
  CHECK_EQUAL(1, array[0]);
  CHECK_EQUAL(2, array[1]);
  CHECK_EQUAL(3, array[2]);
  CHECK_EQUAL(4, array[3]);
  CHECK_EQUAL(5, array[4]);
  CHECK_EQUAL(6, array[5]);
}

TEST(duplicates) {
  // creates a static array with duplicate numbers
  int array[7] = {3, 5, 1, 5, 6, 8, 8};
  mergeSort(array, 6);
  CHECK_EQUAL(1, array[0]);
  CHECK_EQUAL(3, array[1]);
  CHECK_EQUAL(5, array[2]);
  CHECK_EQUAL(5, array[3]);
  CHECK_EQUAL(6, array[4]);
  CHECK_EQUAL(8, array[5]);
  CHECK_EQUAL(8, array[6]);
}

TEST(largeArray) {
  // creates a large dynamically allocated array with alternating low and high values toward the midpoint
  int size = 1000;
  int* array = new int[size];
  
  int j = 0; // set to array[i] and accumulates by 1 when i is even
  int k = size-1; // set to array[i] and decreases by 1 when i is odd

  for(int i = 0; i < size; i++) {
    if(i % 2 == 0) {
      // checks if i is even or odd
      array[i] = j;
      j += 1;
    } else {
      array[i] = k;
      k -= 1;
    }
  }
    
  mergeSort(array, size);
  for(int i = 0; i < size; i++) {
    CHECK_EQUAL(i, array[i]);
  }
  delete[] array;
  array = nullptr;
}

/* no need to modify main */
int main() {
  return UnitTest::RunAllTests();
}
