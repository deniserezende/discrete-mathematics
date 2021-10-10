import random
import random

def generate_items_weight(amount, lower_limit, upper_limit, seed):
    weights = []
    for i in range(0, amount):
        random.seed(seed)
        possible_weight = random.randint(lower_limit, upper_limit)
        while possible_weight in weights:
            possible_weight = random.randint(lower_limit, upper_limit)
        weights.append(possible_weight)
    weights.sort()
    return weights
    
def generate_items_value(amount, lower_limit, upper_limit, seed):
    values = []
    for i in range(0, amount):
        random.seed(seed)
        possible_value = random.randint(lower_limit, upper_limit)
        while possible_value in values:
            possible_value = random.randint(lower_limit, upper_limit)
        values.append(possible_value)
    return values

def generate_knapsack_capacity(weights):
    total = sum(weights)
    lenght = len(weights)
    new_total = total // 2
    if new_total <= weights[lenght-1]:
        new_total = (new_total + weights[lenght-1]) // 2
    return new_total

def max_multiplicities_of_items(kscapacity, weights, values):
    new_weights = []
    new_values = []
    for weight, value in zip(weights, values):
        amount = kscapacity // weight
        for i in range(0, amount):
            new_weights.append(weight)
            new_values.append(value)
    return new_weights, new_values


            
