block_list = [[0 for _ in range(201)] for _ in range(201)]
# offset은 100, -100 ~ 100 -> 0 ~ 200
N = int(input())
for i in range(N):
    x1, y1 = map(int, input().split())
    x1, y1 = x1 + 100, y1 + 100
    x2, y2 = x1 + 8, y1 + 8
    for i in range(x1, x2):
        for j in range(y1, y2):
            block_list[i][j] = 1
# 넓이 구하기
cnt = 0
for i in range(201):
    for j in range(201):
        if(block_list[i][j] == 1):
            cnt += 1
print(cnt)