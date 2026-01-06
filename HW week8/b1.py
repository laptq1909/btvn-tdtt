import math
class cylinder:
    def __init__(self, radius, height):
        self._radius = radius
        self._height = height
    def area(self):
        return 2 * math.pi * self._radius * (self._height + self._radius)
    def volume(self):
        return math.pi * self._radius**2 * self._height
    def __str__(self):
        return f'Area: {self.area():.2f}, Volume: {self.volume():.2f}'
r, h = map(float, input().split())
c = cylinder(r,h)
print(c)