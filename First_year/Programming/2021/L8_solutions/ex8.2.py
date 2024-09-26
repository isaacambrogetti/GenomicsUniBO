def list_cleaning_count(L):
    
    NewL = []
    if len(L) == 0:
        return NewL
    num_elements = 1
    NewL.append(L[0])
    for i in range(1, len(L)):
        if L[i] == L[i - 1]:
            num_elements = num_elements + 1
        else:
            if num_elements >= 2:
                NewL.append(num_elements)
                num_elements = 1
            NewL.append(L[i])
    if num_elements >= 2:
        NewL.append(num_elements)
    return NewL

def inplace_list_cleaning_count(L):
    if len(L) == 0:
        return None

    num_elements = 1
    i = 1
    while i < len(L):
        if L[i] == L[i - 1]:
            del L[i]
            num_elements = num_elements + 1
        else:
            if num_elements >= 2:
                L.insert(i, num_elements)
                i = i + 1
                num_elements = 1
            i = i + 1

    if num_elements >= 2:
        L.insert(i, num_elements)
             