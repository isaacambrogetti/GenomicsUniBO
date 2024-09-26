s1 = input("Insert a string: ")
print(s1 == s1[::-1])


#Alternatively
s2 = input("Insert a string: ")
check_var = True
if len(s2)<2:
    print("True")
else:
    for i in range(len(s2)//2):
        if s2[i] != s2[-1-i]:
            check_var = False
            break
    print(check_var)