N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]
P.sort()
max_student = 0

for i in range(N):
    price = 0
    num_student = 0
    for j in range(N):
        if(i == j):
            price += P[j] / 2
        else:
            price += P[j]
        if(price > B):
            break
        else:
            num_student += 1
    max_student = max(max_student, num_student)

print(max_student)