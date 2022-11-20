/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include "mergeSort.h"

/* merge
 * Merges two ordered arrays, leftArray and rightArray, into one larger ordered array, newArray
 * @param newArray: the new array that will contain an ordered version of lefArray and rightArray
 * @param leftArray: the array containing values for the left half of a list
 * @param leftLength: the length of the left array
 * @param rightArray: the array containing values for right half of a list
 * @param rightLength: the length of the right array
 * i: an integer that increments through the new array
 * leftIndex: an integer that increments through the left array
 * rightIndex: an integer that increments through the right array
 * returns: the combined ordered version of leftArray and rightArray
 */
int* merge(int* newArray, int* leftArray, int leftLength, int* rightArray, int rightLength) {
  int i = 0; 
  int leftIndex = 0; 
  int rightIndex = 0; 

  while(leftIndex < leftLength && rightIndex < rightLength) { 
      
    if(leftArray[leftIndex] < rightArray[rightIndex]) {
      // compares a left array value and right array value to determine with is added to newArray before the other
      newArray[i] = leftArray[leftIndex]; 
      leftIndex += 1; 
      i += 1;
    } else {
      newArray[i] = rightArray[rightIndex];
      rightIndex += 1;
      i += 1;
    }
  }
  
  while(leftIndex < leftLength) {
    // if there are any remaining values in leftArray
    newArray[i] = leftArray[leftIndex]; 
    leftIndex += 1; 
    i += 1;
  }

  while(rightIndex < rightLength) {
    // if there are any remaining values in rightArray
    newArray[i] = rightArray[rightIndex];
    rightIndex += 1;
    i += 1;
  }

  return newArray;
}


void mergeSort(int *array, int length) {
  if(length == 1) {
    return; // when there is only 1 item left in the array
  } 
  
  int leftIndex = 0;
  int rightIndex = length;
  int midPoint = length/2;

  int* leftArray = new int[midPoint]; 
  int* rightArray = new int[rightIndex-midPoint]; 

  for( int i = 0; i < midPoint; i++) {
    leftArray[i] = array[i]; // copies first half of values into the left array
  }
    
  for( int i = midPoint; i < rightIndex; i++) {
    rightArray[i-midPoint] = array[i]; // copies second half of values into the right array
  }

  mergeSort(leftArray, midPoint); 
  mergeSort(rightArray, rightIndex-midPoint);
  
  int* newArray = new int[length]; // array to contain combined sorted arrays 

  newArray = merge(newArray, leftArray, midPoint, rightArray, rightIndex-midPoint);

  for( int i = 0; i < length; i++) {
    array[i] = newArray[i]; // copies values of combined sorted array
  }
    
  delete[] leftArray;
  delete[] rightArray;
  delete[] newArray;
}

 

  



