import math
import secrets
from list_of_primes import bunch_of_primes

# security_parameter is the mesured in bits (size)
# amount_of_primes must be 2 or more.
def generate_keys(security_parameter, amount_of_primes):
    # Calculating the maximum size (in bits) of each of the primes
    prime_size = math.floor(security_parameter/amount_of_primes)

    # This is a private key!
    primes = generate_primes(prime_size, amount_of_primes)

    # This is a public key.
    primes_product = math.prod(primes)

    # Calculating phi   
    primes_minus_one = [prime - 1 for prime in primes]
    phi = math.prod(primes_minus_one)

    # Choosing an integer 'e' such that 1 < e < phi and is a co-prime to phi
    e = choosing_e(phi) # This is a public key.

    # Calculating d (which is the inverse of 'e' mod 'phi')
    d = pow(e, -1, phi) # This is a private key!

    saving_private_keys_in_file(d, primes)

    # Returning the public keys
    return primes_product, e

def saving_private_keys_in_file(d, primes):
    with open("privatekeysdfr.txt", "w+") as file:
        file.write(f"{d}\n")
        for prime in primes:
            file.write("%i\n" % prime)
    file.close()

def generate_primes(size, amount):
    chosen_primes = []
    for i in range(1, amount+1):
        prime = secrets.choice(bunch_of_primes)
        # Choosing another prime
        # until the prime chosen is not already in the list 
        # and the length is less than 'size'
        while (prime in chosen_primes) or (prime.bit_length() > size) or (prime == 2):
            prime = secrets.choice(bunch_of_primes)
        chosen_primes.append(prime)
    return chosen_primes    

def choosing_e(phi):
    possible_e = secrets.SystemRandom().randrange(3, phi)
    while math.gcd(possible_e, phi) != 1:
        possible_e = secrets.SystemRandom().randrange(3, phi)
    return possible_e

####################################################################################################################################
# Functions for the algorithm with both big and small primes
import random
def generate_keys_big_and_small(security_parameter, amount_of_primes):
    # Calculating the maximum size (in bits) of each of the primes
    prime_size = math.floor(security_parameter/amount_of_primes)

    # This is a private key!
    primes = generate_primes_big_and_small(prime_size, amount_of_primes)

    # This is a public key.
    primes_product = math.prod(primes)

    # Calculating phi   
    primes_minus_one = [prime - 1 for prime in primes]
    phi = math.prod(primes_minus_one)

    # Choosing an integer 'e' such that 1 < e < phi and is a co-prime to phi
    e = choosing_e(phi) # This is a public key.

    # Calculating d (which is the inverse of 'e' mod 'phi')
    d = pow(e, -1, phi) # This is a private key!

    saving_private_keys_in_file(d, primes)

    # Returning the public keys
    return primes_product, e

def generate_primes_big_and_small(size, amount):
    amount2 = random.randint(0, amount)
    amount1 = amount - amount2
    size_smaller = 10
    chosen_primes = []
    
    for i in range(1, amount1+1):
        prime = secrets.choice(bunch_of_primes)
        # Choosing another prime
        # until the prime chosen is not already in the list
        # and the length is less than 'size'
        while prime in chosen_primes or prime.bit_length() > size_smaller or prime == 2:
            prime = secrets.choice(bunch_of_primes)
        chosen_primes.append(prime)
    for i in range(1, amount2+1):
        prime = secrets.choice(bunch_of_primes)
        # Choosing another prime
        # until the prime chosen is not already in the list
        # and the length is less than 'size'
        while prime in chosen_primes or prime.bit_length() > size or prime == 2:
            prime = secrets.choice(bunch_of_primes)
        chosen_primes.append(prime)
    return chosen_primes
