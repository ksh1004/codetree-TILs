N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = False

for i in range(N):
    sep = [0 for _ in range(101)]
    for j in range(N):
        if(i == j):
            continue
        else:
            for k in range(grid[j][0], grid[j][1] + 1):
                sep[k] += 1
    for j in range(101):
        if(sep[j] == N - 1):
            answer = True
            break
    if(answer == True):
        break

if(answer):
    print('Yes')
else:
    print('No')        