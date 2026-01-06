class frac:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    def simplify(self):
        gcd = self.greatest_common_divisor(abs(self.numerator), abs(self.denominator))
        self.numerator //= gcd
        self.denominator //= gcd
    def greatest_common_divisor(self, a, b):
        while b:
            a, b = b, a % b
        return a
a, b = map(int, input("Enter numerator and denominator separated by space: ").split())
fraction = frac(a, b)
print(f"Simplified fraction: {fraction.numerator}/{fraction.denominator}")