import math
lst=[]
for i in range(2,101):
    lst.append(i**3)

def cube(a,b,c):
    if (a**3-b**3-c**3) not in lst:
        return False
    elif a**3-b**3-c**3<c**3:
        return False
    return True
    
n=int(input())
for i in range(2,n+1):
    for j in range(2,1+int(n/(3**(1/3)))):
        for k in range(j,n):
            if cube(i,j,k,):
                l=math.ceil((i**3-j**3-k**3)**(1/3))
                print('Cube = {}, Triple = ({},{},{})'.format(i,j,k,l))