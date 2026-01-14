a = list(input().split())
for i in range(len(a)):
    try:
        print(int(a[i]))
    except ValueError:
        print("Not numbers")