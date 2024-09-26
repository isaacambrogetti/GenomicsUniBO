def recursive_min(s):
    if len(s) == 0:
        return None
    elif len(s) == 1:
        return s[0]
    else:
        m = recursive_min(s[1:])
        if s[0] <= m:
            return s[0]
        else:
            return m
        
print(recursive_min([5,3,7,2,10]))
print(recursive_min([11]))
print(recursive_min((15,)))
print(recursive_min((5,3,7,2,10)))
print(recursive_min("somestring"))


