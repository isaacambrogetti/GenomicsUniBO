def Collatz(n):
    if n < 1:
        print("the number must be positive")
    else:
        while n != 1:
            print(n, end=' ')
            if n % 2 == 0:
                n = n//2
            else:
                n = 3*n + 1
        print(n)
   
nbr = int(input("Give me a number! "))
Collatz(nbr)
   