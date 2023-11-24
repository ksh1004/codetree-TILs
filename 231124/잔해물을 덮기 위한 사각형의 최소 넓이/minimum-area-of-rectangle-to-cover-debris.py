block_list = [[0 for _ in range(2001)] for _ in range(2001)]
# A는 넓이 값이 1, B는 2로 두어 A와 B가 겹치는 여부를 파악
# offset: 1000 (-1000 ~ 1000 -> 0 ~ 2000)
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
        block_list[i][j] = 2
# 남은 직사각형 A의 가장 작은/큰 가로, 세로 꼭짓점 구하기
min_x, max_x, min_y, max_y = 2000, 0, 2000, 0
a_value = 0 # 남은 직사각형 A가 있는지 파악하는 변수
for i in range(2001):
    for j in range(2001):
        if(block_list[i][j] == 1): # 남아있다면
            a_value = 1
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)
if(a_value == 1):
    print((max_x - min_x + 1) * (max_y - min_y + 1))
else:
    print(0)