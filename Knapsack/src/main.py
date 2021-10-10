import sys
import time
import Knapsack_Command_Line as COMMANDLINE
import Knapsack_Input_Generator as INPUT
import Knapsack_Dynamic_Programming as DYNAMIC
import Knapsack_Exhaustive_Search as ESEARCH
import Report_Data as REPORT

# COMMAND LINE
amount, lower_weight, upper_weight, lower_value, upper_value, method, report, seed = COMMANDLINE.interpreter(sys.argv)

# INPUT GENERATOR
weights = INPUT.generate_items_weight(amount, lower_weight, upper_weight, seed)
values = INPUT.generate_items_value(amount, lower_value, upper_value, seed)
kscapacity = INPUT.generate_knapsack_capacity(weights)
weights_with_repetitions, values_with_repetitions = INPUT.max_multiplicities_of_items(kscapacity, weights, values)
print(method)
# Starting time
start = time.time()

if method == "DYNAMIC":
    # FINDING BEST SOLUTION WITH DYNAMIC PROGRAMING
    optimal_solution_D, used_items_D = DYNAMIC.get_knapsack_solution(kscapacity, weights_with_repetitions, values_with_repetitions)
    amount_used_items_D = DYNAMIC.count_items_multiplicities(weights, used_items_D)
    
elif method == "ESEARCH":
    # FINDING BEST SOLUTION EXHAUSTIVE SEARCH (BRUTAL FORCE)
    optimal_solution_ES = ESEARCH.get_knapsack_solution(kscapacity, weights_with_repetitions, values_with_repetitions)
elif method == "both":
    # FINDING BEST SOLUTION WITH DYNAMIC PROGRAMING
    startD = time.time()
    optimal_solution_D, used_items_D = DYNAMIC.get_knapsack_solution(kscapacity, weights_with_repetitions, values_with_repetitions)
    amount_used_items_D = DYNAMIC.count_items_multiplicities(weights, used_items_D)
    endD = time.time()
    
    # FINDING BEST SOLUTION EXHAUSTIVE SEARCH (BRUTAL FORCE)
    startES = time.time()
    optimal_solution_ES = ESEARCH.get_knapsack_solution(kscapacity, weights_with_repetitions, values_with_repetitions)
    endES = time.time()

# Ending time
end = time.time()
print(f"{report}")
if report != "no":
    data = []
    data.append(kscapacity)
    data.append(weights)
    data.append(values)
    if method == "DYNAMIC":
        data.append(amount_used_items_D)
        data.append(optimal_solution_D)
        data.append(end-start)
    elif method == "ESEARCH":
        data.append(optimal_solution_ES)
        data.append(end-start)
    elif method == "both":  
        effectiveness = int(optimal_solution_D == optimal_solution_ES)
        data.append(amount_used_items_D)
        data.append(optimal_solution_D)
        data.append(endD-startD)
        data.append(optimal_solution_ES)
        data.append(endES-startES)
        data.append(effectiveness)
    data.append(seed)
    # Saving data in the report
    report_name = "(" + method + ")" + "KnapsackDeniseReport" + str(amount) + ".csv"
    REPORT.generate_report(report, report_name, data)











