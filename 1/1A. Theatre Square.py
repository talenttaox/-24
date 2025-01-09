list= [int(item) for item in input().split()]
a=b=1
if list[0]%list[2]==0:
    a=0
if list[1]%list[2]==0:
    b=0
print((list[0]//list[2]+a)*(list[1]//list[2]+b))