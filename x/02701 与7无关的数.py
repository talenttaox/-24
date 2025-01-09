n=int(input())
k=0
for i in range(1,n+1):
    if i%7==0 or "7" in str(i) :
        pass
    else:
        k+=i**2
print(k)
        