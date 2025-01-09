n=int(input())
for i in range(n):
    num=int(input())
    a=int(input())
    lst_a=[int(x) for x in input().split() if int(x)<num]
    lst_a.sort()
    b=int(input())
    lst_b=[int(x) for x in input().split() if int(x)<num]
    lst_b.sort()
    l=0
    for j in lst_a:
        l+=lst_b.count(num-j)
    print(l)