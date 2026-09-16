from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

start = (0, 0)
end = (N - 1, M - 1)

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if(visited[x][y] == True or grid[x][y] == 0):
        return False
    
    return True

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0 ,0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if(can_go(nx, ny)):
                visited[nx][ny] = True
                q.append((nx, ny))

bfs(start[0], start[1])

if(visited[end[0]][end[1]]):
    print(1)
else:
    print(0)