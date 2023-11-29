s = input()
dx, dy, direction = [0, -1, 0, 1], [1, 0, -1, 0], 0 # 북, 서, 남, 동 순서
x, y = 0, 0
for i in s:
    if(i == 'L'):
        if(direction == 0):
            direction = 1
        elif(direction == 1):
            direction = 2
        elif(direction == 2):
            direction = 3
        elif(direction == 3):
            direction = 0
    elif(i == 'R'):
        if(direction == 0):
            direction = 3
        elif(direction == 1):
            direction = 0
        elif(direction == 2):
            direction = 1
        elif(direction == 3):
            direction = 2
    elif(i == 'F'):
        x, y = x + dx[direction], y + dy[direction]
# 출력
print(x, y)