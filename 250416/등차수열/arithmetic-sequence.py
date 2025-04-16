n = int(input())
a = list(map(int, input().split()))

total = 0

for i in range(1, 101):
    cnt = 0

    for j in range(n):
        for k in range(j + 1, n):
            if(a[j] + a[k] == 2 * i):
                cnt += 1
    
    total = max(total, cnt)

print(total)