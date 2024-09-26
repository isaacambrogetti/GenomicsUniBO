s1 = input("Insert a string: ")
print(s1 == s1[::-1])



s2 = input("Insert a string: ")
check_var = True
if len(s2)<2:
    print("True")
for i in range(len(s2)//2):
    if s2[i] != s2[-1-i]:
        check_var = False
print(check_var)
