class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

N = int(input())
student = []
for i in range(N, 0, -1):
    height, weight = map(int, input().split())
    student.append(Student(height, weight, i))

student.sort(lambda x: (x.height, x.weight, x.number), reverse = True)

for i in student:
    print(i.height, i.weight, (N - i.number + 1))