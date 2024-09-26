import string
s = input("Insert a string: ")
vowels = "aeiouAEIOU"
n_vowels = 0
print("Consonants: ")
for l in s:
    if l in vowels:
        n_vowels = n_vowels + 1
    elif l in string.ascii_letters:
        print(l)
print("Number of vowels: ", n_vowels)