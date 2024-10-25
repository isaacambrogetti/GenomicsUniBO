def Fibonacci(n):
    if n < 1:
        return [0]
    if n == 1:
        return [0, 1]
    if n == 2:
        return [0, 1, 1]

    l = Fibonacci(n-1)
    l.append(l[-1]+l[-2])
    return l

print(Fibonacci(6))