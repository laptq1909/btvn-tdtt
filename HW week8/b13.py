class tri_area:
    def __init__(self, line1, line2, line3):
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
    def triangle_area(self):
        p = (self.line1 + self.line2 + self.line3) / 2
        area = (p * (p - self.line1) * (p - self.line2) * (p - self.line3)) ** 0.5
        return area
    def check(self):
        if (self.line1 + self.line2 > self.line3) and (self.line2 + self.line3 > self.line1) and (self.line1 + self.line3 > self.line2):
            return True
        else:
            return "INVALID"
a, b, c = map(int, input("Enter the lengths of the three sides of the triangle separated by spaces: ").split())
area = tri_area(a, b, c)
if area.check() == True:
    print("The area of the triangle is:", area.triangle_area())
else:
    print(area.check())