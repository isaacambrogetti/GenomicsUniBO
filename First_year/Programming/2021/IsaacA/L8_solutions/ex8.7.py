def print_matrix(M):
    for i in range(len(M)):
        for j in range (len(M[i])):
            print(M[i][j], end='\t')
        print()
        
        
print_matrix([[10000,12], [3,2], [5,6]])        
        