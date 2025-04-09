T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

cnt = 0 # 특별한 위치의 갯수
for i in range(a, b + 1):
    min_d1, min_d2 = 1000, 1000
    for j in range(T):
        if(c[j] == 'S'):
            min_d1 = min(min_d1, abs(i - x[j]))
        elif(c[j] == 'N'):
            min_d2 = min(min_d2, abs(i - x[j]))
    
    if(min_d1 <= min_d2):
        cnt += 1

print(cnt)