import random
n = int(input())
my_list = [random.randint(1, 10) for _ in range(n)]
t = int(input())
try:
    print(my_list[t])
except IndexError:
    print(-1)