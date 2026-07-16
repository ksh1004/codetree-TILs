arr = []
for _ in range(4):
    temp = list(map(int, input().split()))
    arr.append(temp)

cnt = 0
for i in range(4):
    for j in range(4):
        if(arr[i][j] % 5 == 0):
            cnt += 1

print(cnt)