n = input()
v = "aeiouAEIOU"

for i in n:
    if i not in v:
        print(i, end="")