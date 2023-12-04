# ord('A') = 65, ord('Z') = 90
n, m = map(int, input().split())
str_list = [['-' for _ in range(m)] for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동, 남, 서, 북 순서
x, y, direction = 0, 0, 0
# 범위함수
def in_range(x, y):
    return (0 <= x and x < n and 0 <= y and y < m)
# 시뮬레이션 함수
def simulate(x, y, direction):
    s = 65
    for i in range(2, n * m + 1):
        nx, ny = x + dx[direction], y + dy[direction]
        if(in_range(nx, ny) == 1 and str_list[nx][ny] == '-'): # 범위 안에 있고 초기화가 안되었다면
            if(s == 90): # 만약 문자가 Z 이후이면
                s = 65 # A로 초기화
            else:
                s += 1
            str_list[nx][ny] = chr(s) # 문자 저장
        else:
            direction = (direction + 1) % 4 # 방향 전환
            nx, ny = x + dx[direction], y + dy[direction]
            if(s == 90): # 만약 문자가 Z 이후이면
                s = 65 # A로 초기화
            else:
                s += 1
            str_list[nx][ny] = chr(s) # 문자 저장
        x, y = nx, ny # 위치 최신화
# 함수 실행
str_list[x][y] = 'A'
simulate(x, y, direction)
# 출력
for i in range(n):
    for j in range(m):
        print(str_list[i][j], end = ' ')
    print()