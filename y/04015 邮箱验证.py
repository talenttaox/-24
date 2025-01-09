while True:
    try:
        email=input()
    except EOFError:
        break
    judge=True
    list=email.split('@')
    if len(list)!=2:
        judge=False
    else:
        list0=[i for i in list[0]]
        if list0==[] or list0[0]=="."  or list0[-1]==".":
            judge=False
        else:
            list1=list[1].split('.')
            if len(list1)<2 or list1[0]=="" or list1[-1]=="":
                judge=False
    print("YES" if judge else "NO")
        