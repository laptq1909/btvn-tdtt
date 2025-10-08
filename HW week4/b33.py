s = str(int(input("Ex33: ")))
result = ""
count = 0
# Duyệt ngược chuỗi
for i in range(len(s) -1, -1, -1):
    result = s[i] + result
    count += 1
    if count == 3 and i != 0:
        result = '.' + result
        count = 0
print("Số sau khi định dạng:", result)