a=input()
out=""
for i in a:
    if i.isupper():
        out+=i.lower()
    elif i.islower():
        out+=i.upper()
    else:
        out+=i
print(out)