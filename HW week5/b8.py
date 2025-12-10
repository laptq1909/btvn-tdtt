def hamdis(x, y):
    return bin(x ^ y).count('1')
def test():
    assert(hamdis(1, 4) == 2)
    assert(hamdis(3, 1) == 1)
    assert(hamdis(15, 0) == 4)
    assert(hamdis(7, 8) == 4)
if __name__ == "__main__":
    test()
    print("All tests passed.")