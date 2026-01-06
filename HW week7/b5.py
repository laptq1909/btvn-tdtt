n = list(map(int, input().split()))
target = int(input())
count = 0
for i in range(0, len(n)):
    for j in range(i + 1, len(n)):
        if n[i] + n[j] == target:
            count += 1
print(count)