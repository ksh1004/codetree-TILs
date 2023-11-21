class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = 5
person = []
for i in range(n):
    name, height, weight = input().split()
    height, weight = int(height), float(weight)
    person.append(Person(name, height, weight))

person.sort(key = lambda x : x.name)
print('name')
for i in person:
    print(i.name, i.height, i.weight)

print()
print('height')
person.sort(key = lambda x : -x.height)
for i in person:
    print(i.name, i.height, i.weight)