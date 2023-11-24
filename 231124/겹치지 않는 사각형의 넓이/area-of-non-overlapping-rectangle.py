block_list = [[0 for _ in range(2001)] for _ in range(2001)]
# A, B는 넓이 값이 1, M은 2로 두어 A,B와 M이 겹치는 여부를 분리
# offset: 1000 (-1000 ~ 1000 -> 0 ~ 20000)
# 직사각형 A
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000
for i in range(x1, x2):
    for j in range(y1, y2):
        block_list[i][j] = 1
# 직사각형 B
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000
for i in range(x1, x2):
    for j in range(y1, y2):
        block_list[i][j] = 1
# 직사각형 M
x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 + 1000, y1 + 1000, x2 + 1000, y2 + 1000
for i in range(x1, x2):
    for j in range(y1, y2):
        block_list[i][j] = 2
# 넓이 값 계산하기
cnt = 0
for i in range(2001):
    for j in range(2001):
        if(block_list[i][j] == 1):
            cnt += 1
print(cnt)