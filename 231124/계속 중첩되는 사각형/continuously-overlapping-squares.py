block_list = [[0 for _ in range(201)] for _ in range(201)]
# 0은 빨간색, 1은 파란색
n = int(input())
for i in range(n):
    # offset은 100으로, -100 ~ 100 -> 0 ~ 200
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100
    for x in range(x1, x2):
        for y in range(y1, y2):
            if(i % 2 == 0):
                block_list[x][y] = 0
            else:
                block_list[x][y] = 1
# 파란색 영역 넓이 구하기
cnt = 0
for x in range(201):
    for y in range(201):
        if(block_list[x][y] == 1):
            cnt += 1
print(cnt)