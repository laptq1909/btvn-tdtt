a = map(int, input().split())
dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(max(dic, key=dic.get))