#没学会，抄的
import re
def solve(s):
    if re.match(r'R\d+C\d+', s):
        r, c = map(int, s[1:].split('C'))
        res = ''
        while c:
            c, remainder = divmod(c - 1, 26)
            res = chr(65 + remainder) + res
        return res + str(r)
    else:
        pos = 0
        while not s[pos].isdigit():
            pos += 1
        res = 'R' + s[pos:] + 'C'
        c = 0
        for ch in s[:pos]:
            c = c * 26 + ord(ch) - 64
        return res + str(c)

n = int(input().strip())
for _ in range(n):
    s = input().strip().split('\n')[0]
    print(solve(s))