a = map(str, input().split())
dic = {}
for index, i in enumerate(a):
    if i not in dic:
        dic[i] = []
    dic[i].append(index)
for key in dic:
    dic[key] = tuple(dic[key])
print(dic)