answer=[]
def queen(s):
    for i in range(1,9):
        for j in range(len(s)):
            if str(i)==s[j] or abs(i-int(s[j]))==abs(len(s)-j):
                break
        else:
            if len(s)==7:
                answer.append(s+str(i))
            else:
                queen(s+str(i))

queen('')
n=int(input())
for i in range(n):
    b=int(input())
    print(answer[b-1])