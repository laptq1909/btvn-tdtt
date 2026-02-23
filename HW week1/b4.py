a1, b1, c1, a2, b2, a3 = input().split()
a1 = int(a1)
b1 = int(b1)
c1 = int(c1)
a2 = int(a2)
b2 = int(b2)
a3 = int(a3)
ans = ((a1+b1+c1)+(a2+b2) * 2+ a3 * 3) / 10
print(f"{ans:.1f}")