/*
 * Swarthmore College, CS 31
 * Copyright (c) 2021 Swarthmore College Computer Science Department,
 * Swarthmore PA, Professors Tia Newhall, Andrew Danner, and Kevin Webb
 */

//This program plays Game of Life by reading in txt files and displaying 
//the changes made to the board the game is played on. 

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/time.h>
#include <time.h>
#include <string.h>
#include <pthread.h>

/****************** Definitions **********************/
/* Two possible modes in which the GOL simulation can run */
#define OUTPUT_NONE   0   // with no animation
#define OUTPUT_ASCII  1   // with ascii animation

/* Used to slow down animation run modes: usleep(SLEEP_USECS);
 * Change this value to make theh animation run faster or slower
 */
//#define SLEEP_USECS  1000000
#define SLEEP_USECS    100000

/* A global variable to keep track of the number of live cells in the
 * world (this is the ONLY global variable you may use in your program)
 */
static int total_live = 0;

/* This struct represents all the data you need to keep track of your GOL
 * simulation.  Rather than passing individual arguments into each function,
 * we'll pass in everything in just one of these structs.
 * this is passed to play_gol, the main gol playing loop
 *
 * NOTE: You will need to use the provided fields here, but you'll also
 *       need to add additional fields. (note the nice field comments!)
 * NOTE: DO NOT CHANGE THE NAME OF THIS STRUCT!!!!
 */
struct gol_data {

   int rows;  // the row dimension
   int cols;  // the column dimension
   int iters; // number of iterations to run the gol simulation
   int output_mode; // set to:  OUTPUT_NONE, or OUTPUT_ASCII
   int *board; //an array containing the whole board
};

/****************** Function Prototypes **********************/

void *play_gol(void *args);
int init_game_data_from_args(struct gol_data *data, char *argv[]);
void print_board(struct gol_data *data, int round);
int *make_board(struct gol_data *data, int num, FILE *infile);
void update_board(struct gol_data *data);
int check_neighbors(struct gol_data *data, int row, int col, int indx);

/**********************************************************/
int main(int argc, char *argv[]) {

  int ret;
  struct gol_data data;
  double secs, stop, start;

  struct timeval start_time,stop_time;

  if (argc < 3) {
    printf("usage: ./gol <infile> <0|1>\n");
    printf("(0: with no visi, 1: with ascii visi)\n");
    exit(1);
  }

  ret = init_game_data_from_args(&data, argv);
  if(ret != 0) {
    printf("Error init'ing with file %s, mode %s\n", argv[1], argv[2]);
    exit(1);
  }

  ret = gettimeofday(&start_time, NULL);
  if(ret == -1){
    printf("Error with gettimeofday and start_time");
    exit(1);
  }

  data.output_mode = atoi(argv[2]);
  if(data.output_mode == OUTPUT_NONE) {  // run with no animation
    play_gol(&data);

  }
  else { // run with ascii animation
    play_gol(&data);

    if(system("clear")) { 
      perror("clear"); exit(1); 
    }

  
    print_board(&data, data.iters);
  }
  ret = gettimeofday(&stop_time, NULL);
  if(ret == -1){
    printf("Error with gettimeofday and stop_time");
    exit(1);
  }

  secs = 0.0;

  stop = stop_time.tv_sec + (stop_time.tv_usec / 1000000.00);
  start = start_time.tv_sec + (start_time.tv_usec / 1000000.00);
  secs = stop - start;

  // NOTE: do not modify these calls to fprintf
  fprintf(stdout, "Total time: %0.3f seconds\n", secs);
  fprintf(stdout, "Number of live cells after %d rounds: %d\n\n",
      data.iters, total_live);

  free(data.board);
  data.board = NULL;
  return 0;
}
/**********************************************************/
/* initialize the gol game state from command line arguments
 *       argv[1]: name of file to read game config state from
 *       argv[2]: run mode value
 * data: pointer to gol_data struct to initialize
 * argv: command line args
 *       argv[1]: name of file to read game config state from
 *       argv[2]: run mode
 * returns: 0 on success, 1 on error
 */
int init_game_data_from_args(struct gol_data *data, char *argv[]) {
  FILE *infile = NULL;
  int rows, columns, iterations, num;
  int *board;
  int ret;

  infile = fopen(argv[1],"r");
  if(infile == NULL){
    printf("Error: Unable to open file %s \n",argv[1]);
    exit(1);
  }
  ret = fscanf(infile,"%d%d%d%d",&rows,&columns,&iterations,&num);
  if(ret != 4){
    printf("Error: didn't read in rows, cols, iterations, and/or num \n");
    exit(1);
  }
  data->rows = rows;
  data->cols = columns;
  board = make_board(data, num, infile);
  data->board = board;
  data->iters = iterations;

  free(board);
  board = NULL;
    
  return 0;
}
/***************************************
 * This function will dynamically allocate space for a 2D array that will
 * represent the board. This function will also change the live coordinates
 * to 1's as indicated by the text file that is a command line argument.
 *     data: pointer to a struct gol_data
 *     num: int of live coordinates
 *
 *     returns: pointer to 2D array
 */
int *make_board(struct gol_data *data, int num, FILE *infile){
  int *board;
  int i, j;
  int x, y, ret;

  board = malloc(sizeof(int) * (data->rows*data->cols));
  if (board == NULL){
    printf("Error: malloc failed/n");
    exit(1);
  } 
  for(i = 0; i < data->rows; i++){
    for(j = 0; j < data->cols; j++){
      board[i * data->cols + j] = 0;
    }
  }
  for(i = 0; i < num; i++){
    ret = fscanf(infile,"%d%d",&x,&y);
    if (ret != 2){
      printf("Error: didn't read in coordinates");
      exit(1);
    }

    board[x*data->cols + y] = 1;
  }
  
  return board;
}


/**********************************************************/
/* the gol application main loop function:
 *  runs rounds of GOL,
 *    * updates program state for next round (world and total_live)
 *    * performs any animation step based on the output/run mode
 *
 *   data: pointer to a struct gol_data  initialized with
 *         all GOL game playing state
 */
void *play_gol(void *args) {
  struct gol_data *data;
  data = (struct gol_data *)args;

  int iterations = data->iters;

  while (iterations != 0){
    total_live = 0;
    
    if(data->output_mode == 1){
      system("clear");
      print_board(data,iterations);
      usleep(SLEEP_USECS);
    }
    iterations = iterations - 1;
    update_board(data);
  } 
  return NULL;
}
  
/*****************************************************
 * Will change and update the live and dead cells on the board according
 * to the game rules. 
 * Rules:
 *  1. @ with 0 or 1 @ neighbors dies
 *  2. @ with 4+ @ neighbors dies
 *  3. . with 3 @ neighbors becomes alive
 *  4. the rest remain the same
 *
 *  data: pointer to struct gol_data data
 *
 *  side effects: modifies 2D array board 
 */
void update_board(struct gol_data *data){
  int i,j,neighbors,indx;
  int *new_board;

  new_board = malloc(sizeof(int) * (data->rows*data->cols));
  
  for(i = 0; i < data->rows; i++){
   for(j = 0; j < data->cols; j++){ 
    indx = i * data->cols + j;

    neighbors = check_neighbors(data, i,j,indx);

    if(neighbors <= 1 && data->board[i*data->cols + j] == 1){
      new_board[i*data->cols + j] = 0;
    }
    else if (neighbors > 4 && data->board[i*data->cols + j] == 1){
      new_board[i*data->cols + j] = 0;
    }
    else if (neighbors == 3 && data->board[i*data->cols + j] == 0){
      new_board[i*data->cols + j] = 1;
    }
    else{
      new_board[i*data->cols + j] = data->board[i*data->cols + j];
    }
    if(new_board[i*data->cols + j] == 1){
        total_live++;
    }
   } 
  }
  for(i = 0; i < data->rows; i++){
   for(j = 0; j < data->cols; j++){ 
    data->board[i*data->cols + j] = new_board[i*data->cols + j];
   }
  }
  free(new_board);
  new_board = NULL;
}

/********************************************************
 * This functions collects all the neighbors of the current index
 * based on its position on the board. 
 * 
 * data: Pointer to struct gol_data data
 * row: Row of current index
 * col: column of current index
 * indx: current index on the board
 * Returns: number of neighbors for an index
 */
int check_neighbors(struct gol_data *data, int row, int col, int indx){
  int live, cell_above, cell_bottom, cell_right, cell_left,
      cell_above_right, cell_above_left, cell_bottom_left,
      cell_bottom_right;

  if(row == 0){
    //for case where we are in the 1st row
    cell_above = indx + (data->cols * (data->rows - 1));
    if (col == 0){
      //for when we are on the top left cell 
      cell_above_right = cell_above + 1;
      cell_above_left = (data->rows * data->cols) - 1;
      cell_bottom = indx + data->cols;
      cell_bottom_right = indx + data->cols + 1;
      cell_bottom_left = indx + (2*data->cols) - 1;
      cell_left = indx + data->cols - 1;
      cell_right = indx + 1;

    }
    else if (col == data->cols - 1) {
      //for when we are on the top right cell
      cell_above_right = data->cols * (data->rows - 1);
      cell_above_left = cell_above - 1;
      cell_bottom = indx + data->cols;
      cell_bottom_right = indx + 1;
      cell_bottom_left = indx + (data->cols) - 1;
      cell_left = indx - 1;
      cell_right = indx - data->cols + 1;
    }
    else{       //for when we are on the top row in between the corners
      cell_above_left = cell_above - 1;
      cell_above_right = cell_above + 1;
      cell_bottom = indx + data->cols;
      cell_bottom_left = indx + data->cols - 1;
      cell_bottom_right = indx + data->cols + 1;
      cell_left = indx -1;
      cell_right = indx + 1;
    }
  }

  else if(row == data->rows - 1){
    //for case where we are in the last row
    cell_bottom = indx - ((data->rows -1)*data->cols);
    cell_above = indx - data->cols;
    if (col == 0){
      //for case where we are in 1st-column last-row cell
      cell_above_right = indx - data->cols +1;
      cell_above_left = indx - 1;
      cell_bottom_right = cell_bottom + 1;
      cell_bottom_left = data->cols - 1;
      cell_left = indx + data->cols -1;
      cell_right = indx + 1;
    }else if (col == data->cols - 1) {
      //for case where we are in last-column last-row cell
      cell_above_right = indx - (2*data->cols) +1;
      cell_above_left = indx - data->cols - 1;
      cell_bottom_right = 0;
      cell_bottom_left = cell_bottom - 1;
      cell_left = indx -1;
      cell_right = indx - data->cols + 1;
    }else{// for when we are on the last row between the corners
      cell_above_left = cell_above - 1;
      cell_above_right = cell_above + 1;
      cell_bottom_left = cell_bottom - 1;
      cell_bottom_right = cell_bottom + 1;
      cell_left = indx -1;
      cell_right = indx + 1;
    }
  }
  else{//in middle 
    cell_bottom = indx + data->cols;
    cell_above = indx - data->cols;

    if(col == 0){//for case where we are in the 1st column
    cell_left = indx + data->cols - 1;
    cell_above_left = indx - 1;
    cell_bottom_left = indx + (2*data->cols) - 1;
    }
    else{
      cell_left = indx - 1;
      cell_bottom_left = cell_bottom - 1;
      cell_above_left = cell_above - 1;
    }

    if(col == data->cols - 1){//for case where we are in the last column
      cell_right = indx - data->cols + 1;
      cell_above_right = indx - (2*data->cols) + 1;
      cell_bottom_right = indx + 1;
    }
    else{
      cell_right = indx + 1;
      cell_bottom_right = cell_bottom + 1;
      cell_above_right = cell_above + 1;
    }
  }

  
  live = 0;
  if(data->board[cell_right] == 1){//right of index
    live++;
  }
  if(data->board[cell_left] == 1){//left of index
    live++;
  }
  if(data->board[cell_above] == 1){//top of index
    live++;
  }
  if(data->board[cell_bottom] == 1){//bottom of index
    live++;
  }
  if(data->board[cell_above_left] == 1){//top-left of the index
    live++;
  }
  if(data->board[cell_above_right] == 1){//top-right of the index
    live++;
  }
  if(data->board[cell_bottom_left] == 1){//bottom-left of the index
    live++;
  }
  if(data->board[cell_bottom_right] == 1){//top-right of the index
    live++;
  }
  return live;
}

/**********************************************************/
/* Print the board to the terminal.
 *   data: gol game specific data
 *   round: the current round number
 */
void print_board(struct gol_data *data, int round) {

    int i, j;

    fprintf(stderr, "Round: %d\n", round);

    for (i = 0; i < data->rows; ++i) {
        for (j = 0; j < data->cols; ++j) {
          if(data->board[i*data->cols + j] == 1){
            fprintf(stderr, " @");
          }
          if(data->board[i*data->cols + j] == 0){
            fprintf(stderr, " .");
          }
        }
        fprintf(stderr, "\n");
    }
    fprintf(stderr, "Live cells: %d\n\n", total_live);
}
