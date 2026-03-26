n = input("Enter a string : ")
v = "aeiouAEIOU"

for i in n:
    if i not in v:
        print("This is not a vowel", i, end="")
    else:
        print("This is a vowel", i, end="")