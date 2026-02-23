li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
ok = 0
for i in range(len(li2) - len(li1) + 1):
    li = li2[i:i + len(li1)]
    if li == li1:
        ok = 1
        break
if ok: print("YES")
else: print("NO")