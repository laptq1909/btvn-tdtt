a = list(map(int, input().split()))
pos = 0
neg = 0
zero = 0
dic = {'positive': 0, 'negative': 0, 'zero': 0}
for i in a:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1
dic.update({'positive': pos, 'negative': neg, 'zero': zero})
print(dic)