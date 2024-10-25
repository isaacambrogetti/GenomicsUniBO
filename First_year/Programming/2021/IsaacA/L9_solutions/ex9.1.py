def histogram(s):
    D = dict() 
    for c in s:
        if c not in D:
            D[c] = 1
        else:
            D[c] = D[c] + 1
    return D