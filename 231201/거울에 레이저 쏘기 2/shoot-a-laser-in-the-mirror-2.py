N = int(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 남, 서, 북, 동
# / 모양의 경우 0 <-> 1, 2 <-> 3으로 방향 전환
# \ 모양의 경우 0 <-> 3, 1 <-> 2로 방향 전환
str_list = []
# 맵 정보 입력
for i in range(N):
    s = input()
    li = []
    for j in s:
        li.append(j)
    str_list.append(li)
K = int(input()) # 시작 번호
# 레이저 쏘는 위치 계산
x, y, direction = 0, 0, 0
# 시작 위치 및 방향 계산
def start_location(K): # 반환으로 x, y, direction
    if(K <= N): # K <= N
        return 0, K - 1, 0
    elif(K <= 2 * N): # N < K <= 2 * N
        return K - N - 1, N - 1, 1
    elif(K <= 3 * N): # 2 * N < K <= 3 * N
        return N - 1, N - (K - 2 * N), 2
    else: # 3 * N < K
        return N - (K - 3 * N), 0, 3
# 범위함수
def in_range(x, y):
    return (0 <= x and x < N and 0 <= y and y < N)
# 이동함수
def move(x, y, direction):
    nx, ny = x + dx[direction], y + dy[direction]
    return nx, ny
# 시뮬레이션 함수
def simulate(x, y, direction):
    cnt = 0 # 횟수 변수
    while(in_range(x, y)): # 범위 안에 있을 때
        if(str_list[x][y] == '/'): # / 모양의 경우 0 <-> 1, 2 <-> 3으로 방향 전환
            # 방향 먼저 결정
            if(direction == 0):
                direction = 1
            elif(direction == 1):
                direction = 0
            elif(direction == 2):
                direction = 3
            elif(direction == 3):
                direction = 2
            # 방향이 결정되고 나면, 이동
            x, y = move(x, y, direction)
            cnt += 1 # 이동 횟수 1 증가
        else: # \ 모양의 경우 0 <-> 3, 1 <-> 2로 방향 전환
            # 방향 먼저 결정
            direction = 3 - direction
            # 방향이 결정되고 나면, 이동
            x, y = move(x, y, direction)
            cnt += 1 # 이동 횟수 1 증가
    return cnt
# 시뮬레이션 실행
x, y, direction = start_location(K)
cnt = simulate(x, y, direction)
# 출력
print(cnt)