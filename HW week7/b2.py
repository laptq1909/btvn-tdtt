def count_occurrences(arr, x) -> int:
    a = arr.count(x)
    return a
arr = list(map(int, input().split()))
x = int(input())
print(count_occurrences(arr, x))