arr1 = []
arr2 = []

for _ in range(3):
    li = list(map(int, input().split()))
    arr1.append(li)

inp = input()

for _ in range(3):
    li = list(map(int, input().split()))
    arr2.append(li)

for i in range(3):
    for j in range(3):
        print(arr1[i][j] * arr2[i][j], end = ' ')
    print()