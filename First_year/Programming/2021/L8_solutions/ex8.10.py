def prod_matrix_scalar(M, s):
    Ms = []
    for r in M:       # iterate over each row of M
        new_r = []    # build a new from the old row
        for c in r:   # iterate over each element of the row
            new_r.append(c*s) #multiply it by s and add it to the new row
        Ms.append(new_r)  # add the new ro to the new matrix
    return Ms