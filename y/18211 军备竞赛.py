money = int(input())
wapen = [int(x) for x in input().split()]
wapen.sort()
cnt=0
left = 0
right = len(wapen) - 1
while left<=right:
    if wapen[left]<=money:
        cnt += 1
        money -= wapen[left]
        left += 1
    else:
        if right==left:
            break
        money += wapen[right]
        cnt -= 1
        if cnt<0:
            cnt=0
            break
        right -= 1
print(cnt)