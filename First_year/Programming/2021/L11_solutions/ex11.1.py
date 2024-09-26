f = open("L11_solutions/example.txt","r")
lines = f.readlines()
f.close()

f = open("L11_solutions/example.txt","w")
for line in lines:
    nline = line.upper()
    f.write(nline)

f.close()


f = open("L11_solutions/example.txt","w")
for line in lines:
    nline = line.lower()
    f.write(nline)

f.close()

'''OR THIS

f = open("example.txt","w+")
for line in f:
    nline = line.upper()
    f.write(nline)

f.close()
'''
 