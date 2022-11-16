########################################
# CS63: Artificial Intelligence, Lab 2
# Fall 2020, Swarthmore College
########################################

from random import random

def hill_climbing(problem, runs, steps, rand_move_prob):
    """Implementes the hill climbing local search algorithm.
    inputs:
        - problem: A TSP or VRP instance.
        - runs: The number of times to start from a random initial candidate.
        - steps: The number of moves to make in a given run.
        - rand_move_prob: probability of a random neighbor on any given step.
    returns: best_candidate, best_cost
        The best candidate identified by the search and its cost.

    NOTE: Except in the case of a random move, do not call best_neighbor() or
          random_neighbor() directly. Use the get_neighbor() function, which
          has been initialized to point to one of these.
    """
    #initialize best_state and best_cost to a random
    best_state=problem.random_candidate()
    best_cost=problem.cost(best_state)

    for i in range(runs): #restart run runs times
        print("Run: ", i)
        curr_state=problem.random_candidate()
        curr_cost=problem.cost(curr_state)
        for j in range(steps): #check neighbors steps times
            if random()<rand_move_prob: #use random neighbor if probability
                curr_state,curr_cost=problem.random_neighbor(curr_state)
            else: #get best neighbor for TSP, random for VRP
                neighbor_state,neighbor_cost=problem.get_neighbor(curr_state)
                if neighbor_cost<curr_cost:
                    curr_state=neighbor_state
                    curr_cost=neighbor_cost
            if curr_cost<best_cost: #update best_state and best_cost if found a better state
                best_state=curr_state
                best_cost=curr_cost
                print('New best state cost: ',best_cost, " Step: ", j)

    #return best_state and best_cost found
    return best_state,best_cost
