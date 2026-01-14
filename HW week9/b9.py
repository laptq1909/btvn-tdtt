a = input()
try:
    a = int(a)
    print(a)
except ValueError:
    print("Invalid String")