class Point:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number

N = int(input())
point = []
for i in range(1, N + 1):
    x, y = map(int, input().split())
    point.append(Point(x, y, i))

point.sort(key = lambda x: (abs(x.x) + abs(x.y), x.number))

for i in point:
    print(i.number)