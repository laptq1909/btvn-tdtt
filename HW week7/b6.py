flattened = []
lst = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
for sublist in lst:
    for x in sublist:
        flattened.append(x)
print(flattened)