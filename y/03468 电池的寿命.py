while True:
    try:
        n=int(input())
        arr=list(map(int,input().split()))
        tot=sum(arr)
        a=max(arr)
        if a>tot/2:
            print(f"{tot-a:.1f}")
        else:
            print(f"{tot/2:.1f}")
    except EOFError:
        break