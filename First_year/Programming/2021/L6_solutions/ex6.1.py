import math

def isPrime(n):
    if n < 2:
        return False
    i = 2 #check the divisors starting from 2
    #flag =  True # assume the number is prime
    while i <= int(math.sqrt(n)): #check all divisors from 2 to sqrt(n)
        if n % i == 0:
            return False
        i = i+1
    return True 
      
n = int(input("Give me a number! "))
if isPrime(n):
    print(n,"is a prime number")
else:
    print(n,"is NOT a prime number")   