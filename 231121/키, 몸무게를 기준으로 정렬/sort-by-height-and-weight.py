class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
person = []
for i in range(n):
    name, height, weight = input().split()
    height, weight = int(height), int(weight)
    person.append(Person(name, height, weight))

person.sort(key = lambda x: (x.height, -x.weight))
for i in person:
    print(i.name, i.height, i.weight)