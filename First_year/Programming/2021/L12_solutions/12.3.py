print("\n**  Program 3  **\n")

def odd(n):
    if n == 1:         # quello del prof era sbagliato ho dovuto fare la mia versione POLLOOO
        return 1
    n = odd(n-1)
    print(2*n-1)
    return n+1

n = int(input("Type in the number of odd numbers you want:\t"))
odd(n+1)