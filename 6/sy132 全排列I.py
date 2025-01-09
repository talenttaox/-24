def array(index_num,n,used,lst,result):
    if index_num==n+1:
        result.append(lst[:])
        return
    for i in range(1,n+1):
        if not used[i]:
            lst.append(i)
            used[i]=True
            array(index_num+1,n,used,lst,result)
            used[i]=False
            lst.pop()
def output(n):
    result=[]
    used=[False]*(1+n)
    array(1,n,used,[],result)
    for i in result:
        print(' '.join(map(str,i)))
n=int(input())
output(n)