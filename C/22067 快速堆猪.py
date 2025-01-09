a = []
b = []
while True:
    try:
        s = input().split()
        if s[0] == "min":
            if b:
                print(b[-1])
        elif s[0] == "pop":
            if a:
                a.pop()
                if b:
                    b.pop()
        else:
            weight = int(s[1])
            a.append(weight)
            if not b:
                b.append(weight)
            else:
                k = b[-1]
                b.append(min(k, weight))
    except EOFError:
        break