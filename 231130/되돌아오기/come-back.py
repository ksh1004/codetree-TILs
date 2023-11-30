N = int(input())
x, y = 0, 0
dx, dy, direction = [-1, 0, 0, 1], [0, -1, 1, 0], -1 # 서, 남, 북, 동 순서
cnt = 0
idx = -1
for i in range(N):
    v, t = input().split()
    t = int(t)
    if(v == 'W'):
        direction = 0
    elif(v == 'S'):
        direction = 1
    elif(v == 'N'):
        direction = 2
    elif(v == 'E'):
        direction = 3
    for j in range(t):
        cnt += 1
        x, y = x + dx[direction], y + dy[direction]
        if(x == 0 and y == 0):
            idx = cnt
# 출력
print(idx)