########################################
# CS63: Artificial Intelligence, Lab 2
# Fall 2020, Swarthmore College
########################################

from math import exp
from random import random

def simulated_annealing(problem, runs, steps, init_temp, temp_decay):
    """Implements the simulated annealing local search algorithm.
    inputs:
        - problem: A TSP or VRP instance.
        - runs: The number of times to start from a random initial candidate.
        - steps: The number of moves to make in a given run.
        - init_temp: Initial temperature for the start of each run. This should
                scale linearly relative to the cost of a typical candidate.
        - temp_decay: The multiplicative factor by which temperature is reduced
                on each step.
    returns: best_candidate, best_cost
        The best candidate identified by the search and its cost.

    NOTE: In this case, you should always call random_neighbor(), rather than
          get_neighbor() or all_neighbors().
    """
    #initialize best_state and best_cost to a random
    best_state=problem.random_candidate()
    best_cost=problem.cost(best_state)

    for i in range(runs): #restart run runs times
        print("Run: ", i)
        temp=init_temp
        curr_state=problem.random_candidate()
        curr_cost=problem.cost(curr_state)
        for j in range(steps): #check neighbors steps times
            neighbor_state,neighbor_cost=problem.random_neighbor(curr_state)
            delta=curr_cost-neighbor_cost #if positive, found a better state
            if delta>0 or random()<exp(delta/temp): #update if random successor is better or passes probability
                curr_state=neighbor_state
                curr_cost=neighbor_cost
            if curr_cost<best_cost: #update best_state and best_cost if found a better state
                best_state=curr_state
                best_cost=neighbor_cost
                print('New best state cost: ',best_cost,  " Step: ", j)
            temp*=temp_decay

    #return best_state and best_cost found
    return best_state,best_cost
