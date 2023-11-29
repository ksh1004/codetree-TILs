n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1] # 북, 동, 서, 남 순서(남, 북이 서로 반대고, 서, 동이 서로 반대임)
direction = -1 # 방향 설정 변수
# 방향 설정
if(d == 'U'): # 위 (격자에서는 위로 올라가는 것은 값이 줄어드는 것)
    direction = 2
elif(d == 'D'): # 아래 (격자에서는 아래로 내려가는 것은 값이 늘어나는 것)
    direction = 1
elif(d == 'R'): # 오른
    direction = 0
elif(d == 'L'): # 왼
    direction = 3
# 이동 계산
for i in range(t):
    nx, ny = r + dx[direction], c + dy[direction]
    if(nx >= 1 and nx <= n and ny >= 1 and ny <= n): # 이동한 값이 격자 안이라면
        r, c = nx, ny
    else: # 이동한 값이 격자 밖이라면
        direction = 3 - direction # 이동방향 반대방향으로 변경
# 출력
print(r, c)