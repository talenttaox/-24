defi=input()
if defi=="R":
    k=-1
else:
    k=1
str="qwertyuiop[]asdfghjkl;'zxcvbnm,./"
a=input()
str1=""
for i in a:
    str1=str1+str[k+str.index(i)]
print(str1)