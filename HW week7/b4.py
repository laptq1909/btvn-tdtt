def most_occur(n):
    count = {}
    for num in n:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    max_count = max(count.values())
    most_frequent = []
    for num, cnt in count.items():
        if cnt == max_count:
            most_frequent.append(num)
    return min(most_frequent)
n = list(map(int, input().split()))
print(most_occur(n))