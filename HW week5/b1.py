def maxbtw(a, b):
    return max(a, b)
print(maxbtw(10, 20))
def test():
    assert maxbtw(34, 56) == 56
    assert maxbtw(-23, -90) == -23
    assert maxbtw(234, 345) == 345
    assert maxbtw(1, 90) == 90
    assert maxbtw(13, 78) == 78
if __name__ == "__main__":
    test()
    print("All test cases passed!")