try:
    a, b = map(float, input().split())
    print(a + b)
except ValueError:
    print("Not numbers")
finally:
    print("Program ended.")