n = str(input())
m = str(input())
b = len(m)
count = 0
for i in range(len(n)):
    if m == n[i:i+b]:
        count += 1
print(count)