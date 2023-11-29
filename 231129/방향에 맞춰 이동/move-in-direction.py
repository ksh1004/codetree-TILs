N = int(input())
x, y = 0, 0
# 방향 계산
for i in range(N):
    d, v = input().split()
    v = int(v)
    if(d == 'W'):
        x, y = x - v, y
    elif(d == 'S'):
        x, y = x, y - v
    elif(d == 'N'):
        x, y = x, y + v
    elif(d == 'E'):
        x, y = x + v, y
# 출력
print(x, y)