a = input("Ex34 a: ")
b = input("Ex34 b: ")
result = ""
i = 0
while i < len(a):
    if a[i:i + len(b)] == b:
        i += len(b)
    else:
        result += a[i]
        i += 1
print("Chuỗi sau khi xóa:", result)