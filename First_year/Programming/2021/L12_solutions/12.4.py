def t_by_n(t, n):
    if len(t) == 0:
        return ()
    else:
        return (t[0]*n,) + t_by_n(t[1:], n)
 
print(t_by_n((4,2,5,3),2)) 