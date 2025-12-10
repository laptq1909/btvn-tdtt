lst = map(int, input().split())
a = []
sum_num = 0
for i in lst:
    sum_num += i
    a.append(sum_num)
print(a)
