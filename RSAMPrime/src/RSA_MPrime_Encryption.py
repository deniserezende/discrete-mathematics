def get_encryption(primes_product, e, message):
    C = pow(message, e, primes_product)
    return C