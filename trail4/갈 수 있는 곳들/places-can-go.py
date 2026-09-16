from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
start_point = []
visited = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    start_point.append((r - 1, c - 1))

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y):
    if not in_range(x, y):
        return False

    if grid[x][y] == 1 or visited[x][y] == 1:
        return False
    
    return True

def bfs(x, y):
    q = deque()
    visited[x][y] = 1
    q.append((x, y))

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if(can_go(nx, ny)):
                visited[nx][ny] = 1
                q.append((nx, ny))

for start in start_point:
    bfs(start[0], start[1])

cnt = 0
for i in range(N):
    for j in range(N):
        if(visited[i][j]):
            cnt += 1

print(cnt)