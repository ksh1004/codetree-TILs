N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]

people_num = 0
people_nums = []

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False

    return True

def dfs(x, y):
    global people_num

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if(can_go(nx, ny)):
            visited[nx][ny] = True
            people_num += 1
            dfs(nx, ny)
    
for i in range(N):
    for j in range(N):
        if(can_go(i, j)):
            people_num = 1
            visited[i][j] = True
            dfs(i, j)
            people_nums.append(people_num)

people_nums.sort()

print(len(people_nums))
for i in people_nums:
    print(i)