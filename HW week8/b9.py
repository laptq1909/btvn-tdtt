class Student:
    def __init__(self, subject, name):
        self.subject = subject
        self.name = name
        self.score = []
    def add_score(self, score):
        self.score.append(score)
    def avg(self):
        return sum(self.score) / len(self.score)
    def rank(self):
        if self.avg() >= 8:
            return 'excellent'
        elif self.avg() >= 6.5:
            return 'good'
        elif self.avg() >= 5:
            return 'average'
        else:
            return 'poor'
a = input()
n = int(input())
stu = Student(a, 'Student1')
for i in range(n):
    sub, score = input().split()
    stu.add_score(float(score))
print(f"{stu.avg():.2f}")
print(stu.rank())