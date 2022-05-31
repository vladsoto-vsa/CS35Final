/*
  Copyright (c) 2020
  Swarthmore College Computer Science Department, Swarthmore PA
  J. Brody, A. Danner, M. Gagne, L. Meeden, Z. Palmer, A. Soni, M. Wehar
  Distributed as course material for Fall 2020
  CPSC 035: Data Structures and Algorithms
  https://tinyurl.com/yyr8mdoh
*/

#include <fstream>
#include <iostream>
#include <string>

using namespace std;


int lastNum(int*dynamicArray, int length) {
  /* lastNum
    Finds the last number in an array
    Parameters: 
      dynamicArray- array being looked through
      length- length of array, used to index into last value of array
    Return:
      Returns last number in an array

  */
  int last = dynamicArray[length-1];
  return last;
}

int largeNum(int*dynamicArray, int length){
  /* largeNum
    Finds the largest number of an array
    Parameters:
      dynamicArray- array being looked through
      length- length of the array used to search
    Return:
      Returns the largest number in an array
  */
  int large = 0;
  for(int i=0; i<length; i++){
    if (dynamicArray[i]>large) {
      large = dynamicArray[i];
    }
  }
  return large;

}

int lessThan(int* dynamicArray, int length) {
  /* lessThan
      Counts number of values less than 10 in an array
      Parameters:
        dynamicArray- array being looked through
        length- length of array
      Return:
        Returns amount of values less than 10 

  */
  int total = 0;
  for(int i=0; i<length; i++){
    if (dynamicArray[i]<10) {
      total = total + 1;
    }
  }
  return total;
}


double Average(int* dynamicArray, int length){
  /* Average
      Finds the average value of numbers in an array
      Parameters:
        dynamicArray- array being used
        length- length of array being used

      Return:
        Returns average value
  */
  int sum = 0;
  double avrg;
  for(int i=0; i < length; i++) {
    sum += i;
  }
  avrg = double(sum)/length;
  return avrg;
}



int main() {
  /*  Uses returns of lastNum, largeNum, Average, and lessThan
      to print out the last, largest, and average values of an array,
      and number of values less than 10. 

  */
  ifstream myfile;
  string filename; 
  cout << "Please enter the name of your file: ";
  cin >> filename;
  myfile.open(filename);
    
  int number;
  int last;
  int less;
  int largest;
  double avrg;
  
  myfile >> number;
  
  int* dynamicArray;
  dynamicArray = new int [number];
  for (int i = 0; i < number; i++) {
    myfile >> dynamicArray[i];
    //cout << dynamicArray[i] << endl;
  
  }

  avrg = Average(dynamicArray, number);
  less = lessThan(dynamicArray, number);
  last = lastNum(dynamicArray, number);
  largest = largeNum(dynamicArray,number);

  cout << "The last number is " << last << endl;
  cout << "The largest number is " << largest << endl;
  cout << "There are " << less << " numbers less than 10 in the sequence." << endl;
  cout << "The average is " << avrg << endl;
  
  delete[] dynamicArray;
  return 0;

}




