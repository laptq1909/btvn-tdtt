a = list(map(str, input().split()))
k = int(input())
key = []
value = []
dic = {}
dic_new = {}
for i in range(len(a)):
    if i % 2 == 0:
        key.append(a[i])
    else:
        value.append(a[i])
dic = dict(zip(key, value))
for j in dic:
    if dic[j].isdigit():
        if int(dic[j]) > k:
            dic_new[j] = dic[j]
print(dic_new)