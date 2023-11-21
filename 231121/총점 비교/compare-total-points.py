class Score:
    def __init__(self, name, c1, c2, c3):
        self.name = name
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

n = int(input())
score = []
for i in range(n):
    name, c1, c2, c3 = input().split()
    c1, c2, c3 = int(c1), int(c2), int(c3)
    score.append(Score(name, c1, c2, c3))

score.sort(key = lambda x: (x.c1 + x.c2 + x.c3))

for data in score:
    print(data.name, data.c1, data.c2, data.c3)