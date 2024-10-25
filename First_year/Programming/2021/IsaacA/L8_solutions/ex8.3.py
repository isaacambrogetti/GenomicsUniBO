def list_division(A, v):
    lower = []
    greater = []
    for e in A:
        if e <= v:
            lower.append(e)
        else:
            greater.append(e)
    return lower, greater