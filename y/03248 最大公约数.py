try:
    while True:
        a,b=map(int,input().split())
        k=1
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0 and i>k:
                k=i
        print(k)
except EOFError:
    pass