a = list(map(str, input().split()))
dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)