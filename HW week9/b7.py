try:
    a = int(input())
    if a < 0:
        raise ValueError("Invalid age")
    print(2025 - a)
except ValueError:
    print("Invalid age")