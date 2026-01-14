def is_happy_number(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return True

try:
    a = int(input("Nhập số nguyên dương a: "))
    if a <= 0:
        raise ValueError("Số phải là số nguyên dương!")
    if is_happy_number(a):
        print(a, "là số hạnh phúc")
    else:
        print(a, "không phải là số hạnh phúc")
except ValueError as e:
    print("Lỗi nhập liệu:", e)