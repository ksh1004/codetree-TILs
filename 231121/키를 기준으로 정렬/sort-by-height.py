class Info:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

info = []
n = int(input())
for i in range(n):
    name, height, weight = input().split()
    height, weight = int(height), int(weight)
    info.append(Info(name, height, weight))

info.sort(key = lambda x: x.height)
for data in info:
    print(data.name, data.height, data.weight)