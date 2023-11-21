class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

N = int(input())
student = []
for i in range(1, N + 1):
    h, w = map(int, input().split())
    student.append(Student(h, w, i))

student.sort(key = lambda x: (x.height, -x.weight))
for i in student:
    print(i.height, i.weight, i.number)