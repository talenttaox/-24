str="I hate"
n=int(input())
for i in range(1,n):
    if i%2==0 :
        str=str+" that I hate"
    else:
        str=str+" that I love"
str+=" it"
print(str)