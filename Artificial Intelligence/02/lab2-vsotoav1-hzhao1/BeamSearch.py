########################################
# CS63: Artificial Intelligence, Lab 2
# Fall 2020, Swarthmore College
########################################

from math import exp
from numpy.random import choice, multinomial #You should only need one of these.

def choose_neighbors(neighbors,pop_size,temp):
        """Helper function that returns pop_size states in a population list
        inputs:
                - neighbors: A list of tuples (state,cost)
                - pop_size: Number of states to append to pop
                - temp: parameter used to calculate probabilities
        returns: pop
                list of pop_size states
        """
        #initialize list of probabilities corresponding to each candidate
        probs=[]
        sumP = 0
        for state in neighbors: #state: (state,cost)
                cost=-1*state[1]
                p=exp(cost/temp)
                sumP += p
        for state in neighbors: #state: (state,cost)
                cost=-1*state[1]
                p=exp(cost/temp)
                probs.append(p/sumP)


        #select pop_sizes indicies
        indices=list(range(len(neighbors)))
        choices=choice(indices,pop_size,p=probs)

        #convert indices to states
        pop=[]
        for index in choices:
                pop.append(neighbors[index][0]) #selects only state and not cost

        #return list of states
        return pop

def stochastic_beam_search(problem, pop_size, steps, init_temp, temp_decay, \
                           max_neighbors):
    """Implements the stochastic beam search local search algorithm.
    inputs:
        - problem: A TSP or VRP instance.
        - pop_size: Number of candidates tracked.
        - steps: The number of moves to make in a given run.
        - init_temp: Initial temperature. Note that temperature has a slightly
                different interpretation here than in simulated annealing.
        - temp_decay: The multiplicative factor by which temperature is reduced
                on each step. The temperature parameters should be chosen such
                that e^(-cost / temp) never reaches 0.
        - max_neighbors: Number of neighbors generated each round for each
                candidate in the population.
    returns: best_candidate, best_cost
        The best candidate identified by the search and its cost.

    NOTE: In this case, you should always call random_neighbor(), rather than
          get_neighbor() or all_neighbors().
    """
    #initialize best_state and best_cost to a random
    best_state=problem.random_candidate()
    best_cost=problem.cost(best_state)

    #initialize list of pop_size random states
    pop=[]
    for i in range(pop_size):
        pop.append(problem.random_candidate())

    temp=init_temp

    for i in range(steps):
        #list of max_neighbors states for each state in pop

        neighbors=[]
        for state in pop:
                for j in range(max_neighbors):
                        neighbors.append(problem.random_neighbor(state)) #important: appends (state,cost)

        #find overall best neighbor state and cost
        best_neigh_state=neighbors[0][0] #initialize best to first state in neighbors
        best_neigh_cost=neighbors[0][1]
        for state in neighbors[1:]: #state: (state, cost)
                if state[1]<best_neigh_cost:
                        best_neigh_state=state[0]
                        best_neigh_cost=state[1]

        #update best_state and best_cost if found a better state
        if best_neigh_cost<best_cost:
                best_state=best_neigh_state
                best_cost=best_neigh_cost
                print('New best state cost: ',best_cost, " Step: ", i)

        #initialize new population with helper function
        pop=choose_neighbors(neighbors,pop_size,temp)

        temp*=temp_decay

    #return best_state and best_cost found
    return best_state,best_cost
