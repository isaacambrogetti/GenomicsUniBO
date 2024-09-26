a = int(input("First num: "))
b = int(input("Second num: "))

if b == 0:
    print (a)
elif a == 0:
    print (b)
else:
    if a < b:
        smaller = a
    else:
        smaller = b

    for i in range(1, smaller+1):
        if (a % i == 0) and (b % i == 0):
            gcd = i

print (gcd)
