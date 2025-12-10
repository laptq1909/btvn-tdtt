a = map(int, input().split())
k = int(input())
count = 0
ex = 0
for i in a:
    count += 1
    if i == k:
        print(count)
        ex = 1
        break
if ex == 0:
    print(-1)