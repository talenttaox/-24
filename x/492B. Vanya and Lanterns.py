n,l=map(int,input().split())
lst0=list(map(int,input().split()))
lst0.sort()
lst=[-lst0[0]]+lst0+[2*l-lst0[-1]]
lst1=[]
for i in range(n+1):
    lst1.append(lst[i+1]-lst[i])
lst1.sort()
print(f"{(lst1[-1]/2):.9f}")