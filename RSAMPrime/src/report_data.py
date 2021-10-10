# This is a report generator
# if the filename is dot csv, it can be turned into a table.
# Note that you need to specify the separator type as custom, then as ;

def generate_report(report, filename, amount_of_primes, primes, message, time, effectiveness):
    if report == "begin":
        begin_report(filename, amount_of_primes, primes, message, time, effectiveness)
    elif report == "continue":
        continue_report(filename, amount_of_primes, primes, message, time, effectiveness)
    elif report == "end":
        continue_report(filename, amount_of_primes, primes, message, time, effectiveness)

def begin_report(filename, amount_of_primes, primes, message, time, effectiveness):
    file = open(filename, "w+")
    write_in_report(file, amount_of_primes, primes, message, time, effectiveness)
    file.close()

def continue_report(filename, amount_of_primes, primes, message, time, effectiveness):
    file = open(filename, "a")
    write_in_report(file, amount_of_primes, primes, message, time, effectiveness)
    file.close()

def write_in_report(file, amount_of_primes, primes, message, time, effectiveness):
    file.write(f"\n{amount_of_primes};")
    file.write("[")
    for prime in primes:
        if prime == primes[-1]:
            file.write("%i" % prime)
        else:
           file.write("%i, " % prime) 
    file.write("];")
    file.write(f"{message};")
    file.write(f"{time};")
    file.write(f"{effectiveness}")
