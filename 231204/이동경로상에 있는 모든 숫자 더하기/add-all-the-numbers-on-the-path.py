N, T = map(int, input().split())
order_list = input()
num_list = []
for i in range(N):
    num = list(map(int, input().split()))
    num_list.append(num)
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1] # 북, 서, 남, 동 순서
x, y, direction = (N // 2),(N // 2), 0
# L 이동(왼쪽으로 90도 전환)
def L_move(direction):
    direction = (direction + 1) % 4
    return direction
# R 이동(오른쪽으로 90도 전환)
def R_move(direction):
    if(direction == 0): # 방향이 북쪽일 때
        direction = 3 # 동쪽으로 전환
        return direction
    else: # 방향이 북쪽이 아닐 경우
        direction = direction - 1
        return direction
# 범위함수
def in_range(x, y):
    return (0 <= x and x < N and 0 <= y and y < N)
# 시뮬레이션 함수
def simulate(order_list, x, y, direction):
    cnt = 0
    cnt += num_list[x][y] # 처음 서 있는 위치의 값을 더한다.
    for i in order_list:
        if(i == 'L'):
            direction = L_move(direction)
        elif(i == 'R'):
            direction = R_move(direction)
        elif(i == 'F'):
            nx, ny = x + dx[direction], y + dy[direction]
            if(in_range(nx, ny) == 1): # 격자 안에 있는 경우
                cnt += num_list[nx][ny] # 값 추가
                x, y = nx, ny
    return cnt
# 실행
val = simulate(order_list, x, y, direction)
print(val)