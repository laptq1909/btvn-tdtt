n = int(input())
li = list(map(int, input().split()))
ok = 0
ans = 0
for i in range(len(li) - 2, -1, -1):
    if li[i] < li[i + 1]:
        ok = 1
        t = li[i + 1]
        idx = i + 1
        for j in range(i + 1, len(li)):
            if li[j] > li[i]: # Tìm xem số nào lớn hơn vị trí i hiệN tại
                t = min(t, li[j]) # Tìm số lớn hơn vị trí i nhưng phải nhỏ nhất
                idx = j
        li[i], li[idx] = li[idx], li[i]
        #ans 
        ans = li[0: i + 1] + sorted(li[i + 1:])
        break
if ok == 0:
    li.sort()
    print(*li)
else:
    print(*ans)