import random

def interpreter(argv):
	if len(argv) > 0:
	    # Default mode:
	    # dynamic programming
	    # no report
	    # seed is a random value
	    report = "no"
	    method = "DYNAMIC" 
	    seed = random.randrange(100000)
	    for i, arg in enumerate(argv):
	    	# Amount = Necessary
	        if arg == "-a":
	            amount = int(argv[i+1])
	        # Lower Limit Weight = Necessary
	        elif arg == "-LLW": 
	            lower_weight = int(argv[i+1])	            
	    	# Upper Limit Weight = Necessary
	        elif arg == "-ULW": 
	            upper_weight = int(argv[i+1])
	        # Lower Limit Value = Necessary    
	        elif arg == "-LLV": 
	            lower_value = int(argv[i+1])
	        # Upper Limit Value = Necessary
	        elif arg == "-ULV": 
	            upper_value = int(argv[i+1])
	        # Method = optional (there is a default)
	        elif arg == "-ES":
	            method = "ESEARCH"
	        elif arg == "-ESD":
	            method = "both"
	        # Report = optional              
	        elif arg == "-b":
	            report = "begin"
	        elif arg == "-c":
	            report = "continue"
	        elif arg == "-e":
	            report = "end"  
	        elif arg == "-s":
	        	seed = int(argv[i+1])
	return amount, lower_weight, upper_weight, lower_value, upper_value, method, report, seed
