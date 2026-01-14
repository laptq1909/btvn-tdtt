try:
    N = int(input())
    arr = list(map(int, input().split()))
    if len(arr) != N:
        raise ValueError
    for x in arr:
        if x <= 0:
            raise ValueError
    # Kiểm tra phần tử trùng nhau
    if len(set(arr)) != N:
        print("Mang khong hop le")
    else:
        print(sum(arr))
except:
    print("Mang khong hop le")