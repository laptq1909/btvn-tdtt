def calculator(num1, operat, num2):
    if operat == '+':
        result = num1 + num2
    elif operat == '-':
        result = num1 - num2
    elif operat == '*':
        result = num1 * num2
    elif operat == '/':
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    else:
        return "Error: Invalid operator"
    return round(result, 2)
def test():
    assert calculator(10, '+', 5) == 15
    assert calculator(10, '-', 5) == 5
    assert calculator(10, '*', 5) == 50
    assert calculator(10, '/', 2) == 5.0
    assert calculator(10, '/', 0) == "Error: Division by zero"
    assert calculator(10, '^', 5) == "Error: Invalid operator"
    assert calculator(10.567, '+', 5.123) == 15.69
if __name__ == "__main__":
    test()
    print("All tests passed.")