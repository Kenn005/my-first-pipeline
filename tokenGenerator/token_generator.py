#import python's pseudo random number generator
import random

#import time module to access current system time
import time


def generate_token():
    #seed the random number generator using the current system time
    #VULNERABILITY: time.time() is predictable and has low entropy
    random.seed(time.time())

    #generate a 6 digits number between 100000 and 999999
    #VULNERABILITY: output space is very small and can be brute forced
    return str(random.randint(100000,999999)

#calls the function and prints the generated token
#VULNERABILITY:Token generation relies on insecure randomness
print(f"Your token: {generate_token()}")
