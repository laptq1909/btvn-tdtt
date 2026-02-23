arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
def merge(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    if arr1[0]  < arr2[0]:
        return [arr1[0]] + merge(arr1[1:], arr2)
    else:
        return [arr2[0]] + merge(arr1, arr2[1:])
result = merge(arr1, arr2)
print(*result)