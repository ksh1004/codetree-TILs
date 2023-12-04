n = int(input())
num_list = [[0 for _ in range(n)] for _ in range(n)]
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 동, 북, 서, 남 순서
num = (n // 2) # 가운데 값 찾기
x, y, direction = num, num, 0
# 범위함수
def in_range(x, y):
    return (0 <= x and x < n and 0 <= y and y < n)
# 시뮬레이션 함수
# 처음에는 1씩 이동하다가 방향이 왼쪽 혹은 오른쪽으로 바뀔 때, 동일한 방향에 대해 이동거리가 1씩 늘어난다.
# 단, 마지막 끝나는 부분은 그렇지 않다.
def simulate(x, y, direction):
    move = 1
    i = 2
    while(i <= n * n):
        nx, ny = x + dx[direction], y + dy[direction]
        # 이하 if문이나 else문에서 해당 방향으로 주어진 이동거리만큼 이동 후 방향 전환
        if(i != 2 and (direction == 0 or direction == 2)): # 왼쪽 혹은 오른쪽으로 방향이 바뀐 경우
            move += 1 # 이동거리 1 증가
            for j in range(i, i + move): # 이동거리 만큼 for문
                if(j <= n * n): # n * n 안의 값이면
                    num_list[nx][ny] = j # 격자에 값 추가
                    x, y = nx, ny # x, y 좌표 최신화
                if(j != i + move - 1): # j for문에서 마지막 값이 아니면
                    nx, ny = x + dx[direction], y + dy[direction] # nx, ny 새로 입력(num_list의 좌표가 for문에서 이동해야 하므로)
        else: # i == 2 이거나 남, 북으로 이동 시
            for j in range(i, i + move): # 이동거리 만큼 for문
                if(j <= n * n): # n * n 안의 값이면
                    num_list[nx][ny] = j # 격자에 값 추가
                    x, y = nx, ny # x, y 좌표 최신화
                if(j != i + move - 1): # j for문에서 마지막 값이 아니면
                    nx, ny = x + dx[direction], y + dy[direction] # nx, ny 새로 입력(num_list의 좌표가 for문에서 이동해야 하므로)
        i = i + move # i 값을 최신화(이동거리 만큼 추가)
        direction = (direction + 1) % 4 # 방향 전환


# 실행
num_list[x][y] = 1 # 초기값
simulate(x, y, direction) # 실행
# 출력
for i in range(n):
    for j in range(n):
        print(num_list[i][j], end = ' ')
    print()