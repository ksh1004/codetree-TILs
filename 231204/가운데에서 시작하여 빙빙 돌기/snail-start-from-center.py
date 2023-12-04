n = int(input())
num_list = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 동, 북, 서, 남 순서
num = (n // 2) # 가운데 값 찾기
x, y, direction = num, num, 0
# 범위함수
def in_range(x, y):
    return (0 <= x and x < n and 0 <= y and y < n)
# 시뮬레이션 함수
def simulate(x, y, direction):
    for i in range(2, n * n + 1):
        nx, ny = x + dx[direction], y + dy[direction]
        if(in_range(nx, ny) == 1 and num_list[nx][ny] == 0): # 범위 안에 있고 초기화가 안되었다면
            num_list[nx][ny] = i
        else: # 범위 밖인 경우
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]
            num_list[nx][ny] = i
        x, y = nx, ny # 위치 최신화
# 실행
num_list[x][y] = 1
simulate(x, y, direction)
# 출력
for i in range(n):
    for j in range(n):
        print(num_list[i][j], end = ' ')
    print()