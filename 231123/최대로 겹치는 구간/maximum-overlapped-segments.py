n = int(input())
cnt = [0] * 201
for i in range(n):
    x1, x2 = map(int, input().split())
    x1, x2 = x1 + 100, x2 + 100
    for j in range(x1, x2):
        cnt[j] += 1
print(max(cnt))