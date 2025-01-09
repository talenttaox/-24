n= int(input())
num=0
for x in range(n):
    a=input()
    if a.count('1')>=2: num+=1
print(num)