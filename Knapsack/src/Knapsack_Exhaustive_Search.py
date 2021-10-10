import time
import signal

# Custom exception class
class TimeoutException(Exception):  
    pass

# Custom signal handler
def timeout_handler(signum, frame):
    raise TimeoutException

def get_knapsack_solution(kscapacity, weights, values):
    # Change the behavior of SIGALRM
    signal.signal(signal.SIGALRM, timeout_handler)
    # Start the timer, after 'x' seconds, a SIGALRM signal is sent.
    signal.alarm(7200) 
    try:
        temp_solution = [0]
        solution = KNAPSACK(kscapacity, len(weights)-1, weights, values, temp_solution)
        return solution
    except TimeoutException:
        return temp_solution[0]

def KNAPSACK(current_capacity, N, weights, values, temp_solution):
    # Base case: current capacity is less or equal to 0 or there are no more items
    if current_capacity <= 0 or N == -1:
        return(0)

    # Two options: include or not include item 'if it fits!'
    included = 0
    if current_capacity - weights[N] >= 0:
        included = values[N] + KNAPSACK(current_capacity - weights[N], N-1, weights, values, temp_solution)
    excluded = KNAPSACK(current_capacity, N-1, weights, values, temp_solution)
    maximum = max(included, excluded)
    if maximum > temp_solution[0]:
        temp_solution[0] = maximum
    return(maximum)
