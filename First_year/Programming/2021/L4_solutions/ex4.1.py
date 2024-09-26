input_string = input("Insert a string: ")
input_char = input("Insert a character: ")
n = 0
for c in input_string:
    if c == input_char:
        n = n+1
print("The string", input_string, "contains", n, "times the character", input_char)