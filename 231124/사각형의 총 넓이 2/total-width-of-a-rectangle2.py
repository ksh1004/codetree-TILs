block_list = [[0 for _ in range(201)] for _ in range(201)]
N = int(input())
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    # offset은 0~200으로 설정(-100 ~ 100 -> 0 ~ 200)
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100
    for j in range(x1, x2):
        for k in range(y1, y2):
            block_list[j][k] = 1

cnt = 0
for i in range(201):
    for j in range(201):
        if(block_list[i][j] == 1):
            cnt += 1
print(cnt)