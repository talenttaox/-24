n=1
while True:
    p,e,i,d=map(int,input().split())
    if p==e==i==d==-1:
        break
    day=0
    lstp=[]
    lste=[]
    lsti=[]
    for j in range(1,28*33+1):
        lstp.append(p+23*j)
    for j in range(1,23*33+1):
        lste.append(e+28*j)
    for j in range(1,23*28+1):
        lsti.append(i+33*j)
    for k in range(len(lstp)):
        if lstp[k] in lste:
            if lstp[k] in lsti:
                day=lstp[k]-d
                break
    print('Case {}: the next triple peak occurs in {} days.'.format(n,day))
    n+=1