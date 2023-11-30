s = input()
x, y = 0, 0
dx, dy, direction = [0, -1, 0, 1], [1, 0, -1, 0], 0 # 북, 서, 남, 동 순서
cnt = 0 # 이동 시간
idx = -1 # 처음으로 다시 돌아오는 시간 저장
for i in s:
    if(i == 'L'):
        direction = (direction + 1) % 4
        cnt += 1
    elif(i == 'R'):
        if(direction == 0):
            direction = 3
        else:
            direction = direction - 1
        cnt += 1
    elif(i == 'F'):
        cnt += 1
        x, y = x + dx[direction], y + dy[direction]
        if(idx == -1 and x == 0 and y == 0): # 처음으로 제자리에 돌아오는 경우
            idx = cnt
# 출력
print(idx)