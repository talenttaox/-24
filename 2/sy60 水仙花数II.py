def flower(n):
    if (n//100)**3+(n//10%10)**3+(n%10)**3==n:
        return True
    else:
        return False

a,b=map(int,input().split())
lst=[]
for i in range(a,b+1):
    if flower(i):
        lst.append(i)
if len(lst)==0:
    print("NO")
else:
    print(" ".join(map(str,lst)))