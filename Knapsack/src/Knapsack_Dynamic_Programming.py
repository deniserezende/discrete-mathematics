# Pre-condition: same amount of weights and values
def get_knapsack_solution(kscapacity, weights, values):
    knapsack = list(range(0, kscapacity+1))
    columns = len(knapsack)
    rows = len(weights)
    table = [[0 for x in range(0, columns)] for y in range(0, rows)]

    # Creating the first line of the table based on the first weight
    for j in range(0, columns):
        # if weight fits in the knapsack it goes in
        if weights[0] <= knapsack[j]: 
            table[0][j] = values[0]

    for i in range(1, rows, 1): # weights
        for j in range(0, columns, 1): # knapsack
            # Checking if weight fits in the knapsack
            if weights[i] <= knapsack[j]: 
                # Checking if item should be included 
                # aka checking if using the item is the best solution
                if (values[i] + table[i-1][j-weights[i]]) > table[i-1][j]:
                    table[i][j] = (values[i] + table[i-1][j-weights[i]])
                # If not, best solution remains the previous one.  
                else: 
                    table[i][j] = table[i-1][j]
            # If not, best solution remains the previous one.  
            else:
                table[i][j] = table[i-1][j]
    items = get_items_used_in_the_solution(table, kscapacity, weights, values)
    return table[rows-1][columns-1], items

def get_items_used_in_the_solution(table, kscapacity, weights, values):
    items = []    
    columns = kscapacity+1
    rows = len(weights)
    optimal_solution = table[rows-1][columns-1]
    j = columns - 1
    
    for i in range(rows-1, 0, -1):
        # Checking if the best solution is not the same without that element
        if optimal_solution != table[i-1][j]:
            # in that case the element was used. 
            items.append(weights[i])
            # Updating the value of the optiomal solution to the previous one, without that element
            optimal_solution -= values[i]
            # Updating 'j', to acess the column with the previous optiomal solution
            j -= weights[i] 

    # Adding the last value of the optimal solution, in case it was used.
    if values[0] <= optimal_solution:
        items.append(weights[0])
        optimal_solution -= values[0]
    return items

# Receives the weights without repetition and the used weights with repetitions
# and returns a list of the amount of each item used with the same indexes as weights
def count_items_multiplicities(weights, used_weights):
    amount = []
    for weight in weights:
        total_used = used_weights.count(weight)
        amount.append(total_used)
    return amount

def print_table(table, rows, columns):
    for i in range(0, rows, 1): # weights
        for j in range(0, columns, 1): # knapsack
            print(f"[{table[i][j]}] ", end="")
        print("--------------")

