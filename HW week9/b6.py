x = float(input())
try:
    print(f"{x**0.5:.2f}")
except ValueError:
    print("Cannot compute square root of a negative number.")