arr = []
for _ in range(4):
    temp = list(map(int, input().split()))
    arr.append(temp)

cnt = 0
for i in range(0, 4):
    for j in range(i + 1):
        cnt += arr[i][j]

print(cnt)