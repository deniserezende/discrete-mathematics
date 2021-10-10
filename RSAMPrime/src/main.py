import sys
import time
import random
import RSA_MPrime_Keys
import RSA_MPrime_Encryption
import RSA_MPrime_Decryption
import report_data

# Starting time
start = time.time()

def generate_message(primes_product):
    m = random.randint(2, primes_product-1)
    return m

if len(sys.argv) > 0:
    report = "no"
    for i, arg in enumerate(sys.argv):
        if arg == "-a":
            amount = int(sys.argv[i+1])
        elif arg == "-s":
            size = int(sys.argv[i+1])
        elif arg == "-b":
            report = "begin"
        elif arg == "-c":
            report = "continue"
        elif arg == "-e":
            report = "end"
        
public_keys = RSA_MPrime_Keys.generate_keys(size, amount)
message = generate_message(public_keys[0])

encrypted = RSA_MPrime_Encryption.get_encryption(public_keys[0], public_keys[1], message)
decrypted = RSA_MPrime_Decryption.get_decryption(encrypted)

# Ending time
end = time.time()

#print(f"{report}") # This is optional, just a line to follow along.
if report != "no":
    private_keys = RSA_MPrime_Decryption.get_private_keys()
    primes = list(private_keys[1])

    if message == decrypted:
        effectiveness = 1
    else:
        effectiveness = 0

    # Saving data in the report
    report_data.generate_report(report, "RSADeniseReport.csv", amount, primes, message, end-start, effectiveness)

#RSA_MPrime_Decryption.remove_pendencies() # This is optional!
