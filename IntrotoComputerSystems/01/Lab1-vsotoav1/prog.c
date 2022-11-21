/*
 * Swarthmore College, CS 31
 * Copyright (c) 2021 Swarthmore College Computer Science Department,
 * Swarthmore PA, Professor Tia Newhall and Andrew Danner
 */

/*
 * Name: Vladimir Soto-Avina
 * CS31 Spring 21
 * This program finds the average of randomized values in a range limited by the user's input and amount of values.
 * Furthermore, it prints a pyramid based on the user's int input between a set range.
 * 
 */

/* C libraries are included here */
#include <stdio.h>      // the C standard I/O library
#include <stdlib.h>     // the C standard library
#include <time.h>       // time library, used to seed random num generator

/* define constant values here */
#define MAX  30        // the max size of the picture  

/* function prototypes go here */
int read_int(char *msg);  /* these are defined for you */

/* TODO: add other function prototypes here: */
float compute_average(int num, int high);
int get_in_range(int lo, int hi);
void draw_picture(int size);

/***********************************************************/
int main (int argc, char *argv[]) {

  /* declare all local variables at the top of the function body */
  int num, high, size, answer; 
  float average;
  int lo = 3;

  
  srand(time(0));


  /* TODO: add main program control flow code here, starting
   * with editing this printf stmt to say what the program does
   * (you can add more printf stmts for this if the line gets too long)
   */
  printf("This program computes the average of random values, the amount selected by the user. \nFurthermore, it draws a pyramid based on the user's input for size. \n");
         
         
  num = read_int("Enter number of values to average: ");
  high = read_int("Enter high end of range of values: ");
  average = compute_average(num,high);
  printf("The average of %d random values in the range [0,%d] is %f. \n", num, high, average);


  size = get_in_range(lo,MAX);
  draw_picture(size);
  printf("Another drawing? Enter 0 for no or 1 for yes: \n");
  answer = read_int("Answer: ");


  while (answer != 1 && answer != 0){
    printf("0 nor 1 were entered. Enter 0 or 1 \n");
    answer = read_int("Answer:  ");
  }

  while (answer == 1){
    int size = get_in_range(lo,MAX);
    draw_picture(size);
    printf("Another drawing? Enter 0 for no or 1 for yes: \n");
    answer = read_int("Answer: ");
  }
  
  if (answer == 0){
    printf("Goodbye \n");
  }
  return 0;
}

/*
  * compute_average: prompts user to enter amount of int values they want to average
  *                  and highest value allowed in a that range, which then returns the average 
  *                  of random values. 
  * num = amount of values to be averaged (denominator)
  * high = highest int value in range of randomized values
  * returns: average float value of randomized int values
  * 
  * 
*/ 
float compute_average(int num,int high){
  float total = 0;
  float average;
  for (int i=1; i<=num; i++){
    int randValue = rand();
    int val;
    val = randValue % (high + 1);
    total = total + val;
  }
 average = total / num;
 return average;
}

/*
  * get_in_range: prompts user to enter an integer value between two set
  *               integer values
  * lo: lowest value in range
  * hi: highest value in range
  * returns: allowed integer value between lo and hi. 

*/

int get_in_range(int lo, int hi){
  printf("Enter a value between %d and %d. \n", lo,hi);
  int val = read_int("Value: ");

  while (val < lo || val > hi){
    printf("Value was not between the low and the high values \n");
    val = read_int("Value: ");
  }
  return val;
}

/*
  * draw_picture: based on integer value entered in prompt, 
  *               prints a pyramid of the integer size
  * size: integer value returned from get_in_range
*/
void draw_picture(int size){
  for (int row_number=1;row_number<=size;row_number++){  
    
    for (int spaces=0;spaces<=size-row_number;spaces++){
      printf(" ");
    }

    for (int stars=1;stars<=(row_number*2)-1;stars++){
      printf("*");
    }

    for (int spaces=0;spaces<=size-row_number;spaces++){
      printf(" ");
    }
      
    printf("\n");
  }
}


/* THIS FUNCTION IS PROVIDED FOR YOU: DO NOT MODIFY! */
/******************************************
 * read_int: prompts the user to enter an integer value, 
 *           and returns to the entered value to the caller
 *  msg: the prompt msg to print
 *       (char * is the type for C strings, don't worry about understanding 
 *        the char * type now, we will talk about it later)
 *  returns: int value entered by user
 *
 * NOTE: this function is NOT robust to bad user input
 */
int read_int(char *msg) {

  int val;

  printf("%s", msg);
  scanf("%d", &val);
  return val;
}


