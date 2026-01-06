pairs = []
labels = ['A', 'B', 'C', 'D']
for i in range(4):
    phrase = input().strip()
    pairs.append((phrase, labels[i]))
pairs.sort()
result = []
for _, label in pairs:
    result.append(label)
print(" ".join(result))