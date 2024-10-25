def transpose(M):
    MT = []
    nr = len(M)   # number of rows
    if nr == 0:    #empty
        return MT
    else:
        nc = len(M[0])  # number of columns
        for i in range(nc): 
            col = []
            for j in range(nr): #loop on rows
                col.append(M[j][i])  # collect all the rows j of column i
            MT.append(col)      # fill a matrix by the columns of M
        return MT

def scalar_prod(U, V):
    if len(U) == len(V):
        res = 0
        for i in range(len(V)):
            res = res + (U[i] * V[i])
        return res
    else:
        return None
    
def prod_matrices(A,B):
    if len(A[0]) == len(B):  # check if #cols(A) = #row(B)
        AB = []
        BT = transpose(B)          # transpose B
        for i in range(len(A)):    # iterate over the rows from A
          row = []                 # creat a new row for AB
          for j in range(len(BT)): # iterate over the rows from BT
                sp = scalar_prod(A[i],BT[j]) # compute scalar product of two lists 
                row.append(sp)     # insert the new element in the new row
          AB.append(row)           # insert the new row in the final matrix
        return AB
    else:
        return None