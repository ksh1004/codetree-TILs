n, m = map(int, input().split())
num_list = [[0 for _ in range(m)] for _ in range(n)] # n * m 직사각형
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # 남, 동, 북, 서 순서
# 범위함수
def in_range(x, y):
    return (0 <= x and x < n and 0 <= y and y < m)
# 시뮬레이션 함수
def simulate(x, y, direction):
    for i in range(2, n * m + 1):
        nx, ny = x + dx[direction], y + dy[direction]
        if(in_range(nx, ny) and num_list[nx][ny] == 0): # 이동한 격자가 범위 안이고 아직 값이 안채워져 있으면
            x, y = nx, ny
            num_list[x][y] = i
        else: # 이동한 격자가 범위 밖이면
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]
            x, y = nx, ny
            num_list[x][y] = i
# 시뮬레이션 실행
x, y, direction  = 0, 0, 0 # 초기값
num_list[x][y] = 1
simulate(x, y, direction) # 실행
# 출력
for i in range(n):
    for j in range(m):
        print(num_list[i][j], end = ' ')
    print()