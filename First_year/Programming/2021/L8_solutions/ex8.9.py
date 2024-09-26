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


   
