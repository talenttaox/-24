def find_coin(judge):
    for i in range(12):
        for j in range(2):
            coin=[0]*12
            coin[i]=2*j-1
            times=0
            for k in range(3):
                left,right,s=judge[k][0],judge[k][1],judge[k][2]
                sum_left=0
                for l in left:
                    sum_left+=coin[ord(l)-65]
                sum_right=0
                for l in right:
                    sum_right+=coin[ord(l)-65]
                if s=='even' and sum_left==sum_right:
                    times+=1
                elif s=='up' and sum_left>sum_right:
                    times+=1
                elif s=='down' and sum_left<sum_right:
                    times+=1
            if times==3:
                return (i,j)
n=int(input())
for i in range(n):
    judge=[]
    for i in range(3):
        judge.append(list(map(str,input().split())))
    x,y=find_coin(judge)
    a=chr(65+x)
    b='heavy' if y==1 else 'light'
    print('{} is the counterfeit coin and it is {}.'.format(a,b))


