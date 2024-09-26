import string
input_string = input("Insert a string: ")
clean_string = ''
for c in input_string:
    if c not in string.punctuation and c not in string.whitespace:
        clean_string = clean_string+c
print(clean_string)