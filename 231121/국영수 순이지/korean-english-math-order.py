class Score:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

n = int(input())
score = []
for i in range(n):
    name, korean, english, math = input().split()
    korean, english, math = int(korean), int(english), int(math)
    score.append(Score(name, korean, english, math))

score.sort(key = lambda x: (x.korean, x.english, x.math), reverse = True)

for data in score:
    print(data.name, data.korean, data.english, data.math)