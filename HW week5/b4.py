def perfect(n):
    lst = []
    for i in range(1, int(n/2 + 1)):
        if n % i == 0:
            lst.append(i)
    if sum(lst) == n:
        return True
    else:
        return False
def test():
    assert perfect(23) == False
    assert perfect(6) == True
    assert perfect(28) == True
    assert perfect(123) == False
    assert perfect(24) == False
if __name__ == "__main__":
    test()
    print("All tests passed.")