n, m = map(int, input().split())
num_list = [[0 for _ in range(m)] for _ in range(n)] # n * m 사각형
x, y = 0, 0
num_list[x][y] = 1 # 초기값
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 오른쪽, 아래, 왼쪽, 위 순서
direction = 0
for i in range(2, n * m + 1):
    nx, ny = x + dx[direction], y + dy[direction]
    # 격자 바깥인지 혹은 이미 해당 값이 있는지 확인
    if((nx < 0 or nx >= n or ny < 0 or ny >= m) or (num_list[nx][ny] != 0)):
        direction = (direction + 1) % 4
    # 다음 위치로 이동(위의 nx, ny와 혼동하지 않도록 주의)
    x, y = x + dx[direction], y + dy[direction]
    num_list[x][y] = i
# 출력
for i in range(n):
    for j in range(m):
        print(num_list[i][j], end = ' ')
    print()