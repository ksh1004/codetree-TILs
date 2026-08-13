from collections import deque
import sys

def solve():
    data = sys.stdin.read().split('\n')
    grid = [data[i] for i in range(10)]

    start = end = None
    blocked = None

    for r in range(10):
        for c in range(10):
            ch = grid[r][c]
            if ch == 'L':
                start = (r, c)
            elif ch == 'B':
                end = (r, c)
            elif ch == 'R':
                blocked = (r, c)

    # BFS
    visited = [[False] * 10 for _ in range(10)]
    dist = [[0] * 10 for _ in range(10)]
    q = deque([start])
    visited[start[0]][start[1]] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()
        if (r, c) == end:
            break
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < 10 and 0 <= nc < 10:
                if not visited[nr][nc] and (nr, nc) != blocked:
                    visited[nr][nc] = True
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

    # dist[end]는 이동 횟수(간선 수) → 중간 칸 개수는 -1
    print(dist[end[0]][end[1]] - 1)

solve()