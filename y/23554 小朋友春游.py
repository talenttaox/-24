n=int(input())
lst=[int(i) for i in input().split()]
lst.sort()
lst1=[i for i in range(1,n+1) if i not in lst]
lst2=lst[n-len(lst1):]
print(" ".join(map(str,lst1)))
print(" ".join(map(str,lst2)))