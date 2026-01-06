def mul(re1, im1, re2, im2):
    return (re1 * re2 - im1 * im2, re1 * im2 + im1 * re2)
re1, im1 = map(int, input().split())
re2, im2 = map(int, input().split())
result = mul(re1, im1, re2, im2)
print(f"{result[0]} {result[1]}")