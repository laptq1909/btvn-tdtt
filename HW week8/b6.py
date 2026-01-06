class rectangle:
    def __init__(self, width, height, factor):
        self.width = width
        self.height = height
        self.factor = factor
    def scale(self):
        self.width *= self.factor
        self.height *= self.factor
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
w, h, k = map(int, input().split())
rec = rectangle(w, h, k)
rec.scale()
print(f"{rec.area():.2f}")
print(f"{rec.perimeter():.2f}")