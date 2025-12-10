def is_isomorphic(a, b):
    map_ab = {}
    map_ba = {}
    
    for ch1, ch2 in zip(a, b):
        if ch1 in map_ab and map_ab[ch1] != ch2:
            return False
        if ch2 in map_ba and map_ba[ch2] != ch1:
            return False
        map_ab[ch1] = ch2
        map_ba[ch2] = ch1
    return True
def test():
    assert is_isomorphic("egg", "add") == True
    assert is_isomorphic("foo", "bar") == False
    assert is_isomorphic("paper", "title") == True
    assert is_isomorphic("ab", "aa") == False
    assert is_isomorphic("", "") == True
    assert is_isomorphic("a", "b") == True
    assert is_isomorphic("abc", "def") == True
    assert is_isomorphic("abc", "dee") == False
if __name__ == "__main__":
    test()
    print("All tests passed.")