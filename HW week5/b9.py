def sum_num(n):
    n = str(n)
    a = 0
    for i in n:
        a += int(i)
    return a
def test():
    assert sum_num(123) == 6
    assert sum_num(0) == 0
    assert sum_num(9999) == 36
if __name__ == "__main__":
    test()
    print("All tests passed.")