a = {}
m = map(str, input().split())
for i in m:
    k, v = i.split(':')
    if k not in a:
        a[k] = [v]
    else:
        a[k].append(v)
print(a)