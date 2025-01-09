n=int(input())
wood=[[int(x) for x in input().split()] for i in range(n)]
count=2
if n==1:
    print(1)
else:
    for i in range(1,n-1):
        if wood[i][0]-wood[i-1][0]>wood[i][1]:
            count+= 1
        elif wood[i+1][0]-wood[i][0]>wood[i][1]:
            count+=1
            wood[i][0]+=wood[i][1]    
    print(count)