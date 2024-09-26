def ascending_order(L):
    if len(L) == 0:
        return True
    for i in range(1, len(L)):
        if L[i] < L[i-1]:
            return False
    return True