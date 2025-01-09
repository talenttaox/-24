from collections import Counter  
n=int(input())
lst=[int(x) for x in input().split()]
c=Counter(lst)
a,b=c.most_common(1)[0]
print(b)