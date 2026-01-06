class live:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Lies(self):
        if self.x == 0 and self.y == 0:
            return "Origin"
        elif self.x == 0:
            return "Y Axis"
        elif self.y == 0:
            return "X Axis"
        else:
            return None
    def Distance(self):
        return (self.x**2 + self.y**2)**0.5
x, y = map(int, input().split())
point = live(x, y)
print(point.Lies())
print(f"{point.Distance():.2f}")