n,m=map(int,input().split())
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
lst=lst1+lst2
lst.sort()
print(' '.join(map(str,lst)))