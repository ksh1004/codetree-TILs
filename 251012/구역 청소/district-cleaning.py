a, b = map(int, input().split())
c, d = map(int, input().split())
sep = [0 for _ in range(101)]

for i in range(a, b):
    sep[i] = 1
for j in range(c, d):
    sep[j] = 1

cnt = 0
for k in range(0, 101):
    if(sep[k] == 1):
        cnt += 1

print(cnt)