def remove_element(L, e):
    if L == []:
        return []
    if e not in L:
        #return L.copy()# WHY copy?
        return L
    LR = remove_element(L[1:], e)
    if L[0] == e:
        return LR
    else:
        return [L[0]] + LR

L =  [3,5,7,3,1,2,3,8,9]    
e = 10
L1= remove_element(L, e)
print("Org list: ", L)
print("New list: ", L1)

#L1.append(100)
#print("Org list: ", L)
#print("New list: ", L1)