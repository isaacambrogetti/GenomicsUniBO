def repeat(L):
    L_new = list()
    for e in L:
        L_new = L_new+ [e]*e
    return L_new

def inplace_repeat(L):
    i = 0
    while i < len(L):
        e = L[i]
        L[i+1:i+1] = [e]*(e-1)  
        i = i + e
        