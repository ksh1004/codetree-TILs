arr = []
for i in range(4):
    temp = list(map(int, input().split()))
    arr.append(temp)

for i in range(4):
    cnt = 0
    for j in range(4):
        cnt += arr[i][j]
    print(cnt)