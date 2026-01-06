def Selection_sort(n):
    for i in range(len(n)):
        min_index = i
        for j in range(i + 1, len(n)):
            if n[j] < n[min_index]:
                min_index = j
        n[i], n[min_index] = n[min_index], n[i]
    return n
n = list(map(int, input().split()))
print(Selection_sort(n))