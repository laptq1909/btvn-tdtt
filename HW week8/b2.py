class date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def display(self):
        if self.month < 1 or self.month > 12:
            return "Invalid"
        if self.day < 1 or self.day > 31:
            return "Invalid"
        if self.month == 2 and self.day > 28:
            return "Invalid"
        if self.month in {4, 6, 9, 11} and self.day > 30:
            return "Invalid"
        if self.month in [1, 3, 5, 7, 8, 10]:
            if self.day == 31:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        elif self.month == 2:
            if self.day == 28:
                self.day = 1
                self.month += 1
            else:
                self.day += 1
        elif self.month in [4, 6, 9, 11]:
            if self.day == 30:
                self.day = 1
                self.month += 1
        elif self.month == 12:
            if self.day == 31:
                self.day = 1
                self.month = 1
                self.year += 1
            else:
                self.day += 1
        return f"{self.day}/{self.month}/{self.year}"
day, month, year = map(int, input().split())
d = date(day, month, year)
print(d.display())