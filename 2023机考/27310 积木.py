n=int(input())
block=[]
s=[1234,1243,1324,1342,1423,1432,2134,2143,2314,2341,2413,2431,3124,3142,3214,3241,3412,3421,4123,4132,4213,4231,4312,4321]
                            
for i in range(4):
    block.append(input())
for i in range(n):
    judge=False
    word=input()
    k=len(word)
    for i in s:
        num=0
        for j in range(k):
            if word[j] in block[int(str(i)[j])-1]:
                num+=1
        if num==k:
            judge=True
            break
    print('YES' if judge else 'NO')
