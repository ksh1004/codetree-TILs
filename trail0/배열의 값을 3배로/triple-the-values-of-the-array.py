arr = []
for _ in range(3):
    li = list(map(int, input().split()))
    arr.append(li)

for i in range(3):
    for j in range(3):
        print(arr[i][j] * 3, end = ' ')
    print()