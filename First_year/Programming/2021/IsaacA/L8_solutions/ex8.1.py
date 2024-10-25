def list_cleaning(A):
    
    NewA = []
    if len(A) == 0:
        return NewA
    NewA.append(A[0])
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            NewA.append(A[i])
    return NewA

def inplace_list_cleaning(A):
   
    if len(A) == 0:
        return None
    i = 1
    while i<len(A):
        if A[i] == A[i-1]:
            del A[i]
        else:
            i =  i + 1
            
# This is wrong, why?             
def wrong_list_cleaning(A):
    for i in range(1,len(A)):
        if A[i] == A[i-1]:
            del A[i]            