def fac(n):
    if n == 0:
        return 1
    for i in range(1, n):
        n *= i
    return n
def test_fac():
    assert fac(5) == 120
    assert fac(0) == 1
    assert fac(1) == 1
    assert fac(3) == 6
    assert fac(4) == 24
if __name__ == "__main__":
    test_fac()
    print("All tests passed.")