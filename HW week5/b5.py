def placement(a, k):
    for i in range(len(a)):
        if a[i] == k:
            return i + 1
    return -1
def test():
    assert placement([1, 2, 3, 4, 5, -6, 7, 8, 19, 1, 2, 3, 4, 5], 3) == 3
    assert placement([10, 20, 30], 10) == 1
    assert placement([7, 8, 9], 5) == -1
    assert placement([], 1) == -1
    assert placement([1, 2, 3, 4, 5], 6) == -1
if __name__ == "__main__":
    test()
    print("All tests passed.")