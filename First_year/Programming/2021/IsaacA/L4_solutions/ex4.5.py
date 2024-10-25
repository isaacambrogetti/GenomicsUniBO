n = int(input("Insert a number: "))
for j in range(1,n+1):
    for i in range(0,11):
        print(j, "x", i, "=", j*i)
    print(" ")