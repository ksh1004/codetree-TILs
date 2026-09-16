N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False for _ in range(N)] for _ in range(N)]

people_num = 0
people_nums = list()

# 주어진 위치가 격자 내부에 있는지 확인
def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

# 주어진 위치로 이동할 수 있는지 여부
def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False

    return True

def dfs(x, y):
    global people_num

    # 우 하 좌 상
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
    
        if can_go(nx, ny):
            visited[nx][ny] = True
            people_num += 1
            dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if can_go(i, j):
            visited[i][j] = True
            people_num = 1

            dfs(i, j)

            people_nums.append(people_num)

people_nums.sort()

print(len(people_nums))

for i in range(len(people_nums)):
    print(people_nums[i])