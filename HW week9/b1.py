a, b = map(int, input().split())
try:
    print(f"{a}/{b}={a/b:.2f}")
except ZeroDivisionError:
    print("Error: Division by zero")