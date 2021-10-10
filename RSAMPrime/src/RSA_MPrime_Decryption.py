import ChineseRemainderTheorem
import os

def get_decryption(ciphertext):
    # 'd' is the inverse of 'e' mod 'phi'
    # 'e' is a coprime of 'phi'
    # 'phi' is the product whose factors are each prime minus 1
    d, primes = get_private_keys()

    # ds is a list that contains the values of
    # ds[i] = d % (primes[i] - 1)
    ds = calculates_ds(d, primes) 
    
    # Ms is a list that contains the values of
    # Ms[i] = (ciphertext**d[i]) % primes[i]
    Ms = calculate_Ms(ciphertext, ds, primes)
    
    message = ChineseRemainderTheorem.CRT(Ms, primes)

    return message;

def get_private_keys():
    file = open("privatekeysdfr.txt", "r")
    lines = file.readlines()
    file.close()
    temp = []
    for line in lines:
        temp.append(int(line))    
    d = temp[0]
    primes = temp[1:]
    return d, primes


def calculates_ds(d, primes):
    ds = []
    for prime in primes:
        ds.append(d % (prime - 1))
    return ds

def calculate_Ms(ciphertext, ds, primes):
    Ms = []
    for d, prime in zip(ds, primes):
        Ms.append(pow(ciphertext, d, prime))
    return Ms

def remove_pendencies():
    os.remove("privatekeysdfr.txt")
