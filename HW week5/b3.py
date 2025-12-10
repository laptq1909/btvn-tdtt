def isprime(n):
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True
def test():
    assert isprime(2) == True
    assert isprime(3) == True
    assert isprime(10) == False
    assert isprime(9) == False
    assert isprime(13) == True
if __name__ == "__main__":
    test()
    print("All tests passed.")