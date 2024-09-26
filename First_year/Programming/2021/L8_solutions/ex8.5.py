def merge_sorted(L1, L2):
    LR = []
    i = 0
    j = 0
    while i<len(L1) and j<len(L2):
        if L1[i] <= L2[j]:
            LR.append(L1[i])
            i += 1
        else:
            LR.append(L2[j])
            j += 1

    if i < len(L1):
        LR = LR + L1[i:]
    else:
        LR = LR + L2[j:]

    return LR