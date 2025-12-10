def swap(a, b):
    return b, a
print(swap(5, 10))
def test():
    assert swap(12, -30) == (-30, 12)
    assert swap(13, 10) == (10, 13)
    assert swap(45, 12) == (12, 45)
    assert swap(10, 90) == (90, 10)
    assert swap(100, 45) == (45, 100)
if __name__ == "__main__":
    test()
    print("All test cases passed!")