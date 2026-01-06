n = int(input())
lst = []
for i in range(n):
    a = input()
    lst.append(a)
for i in range(0, len(lst)):
    if lst[i] == "Nemo":
        print(f"{lst[i-1]} and {lst[i+1]}")
        break