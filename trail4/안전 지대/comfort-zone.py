import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)] # 방문 여부
K = 0 # 최대로 가능한 K값
max_num = -1 # 최대로 가능한 안전 영역의 수
num = 0 # i일 때 안전 영역 수
def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y, K):
    if not in_range(x, y):
        return False
    
    if visited[x][y] == True or grid[x][y] <= K:
        return False
    
    return True

def dfs(x, y, K):
    global num

    #상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if(can_go(nx, ny, K)):
            visited[nx][ny] = True
            dfs(nx, ny, K)
    

for i in range(1, 100):
    num = 0 # i일 때 안전 영역 수
    visited = [[False for _ in range(M)] for _ in range(N)] # 방문 여부 초기화
    for j in range(N):
        for k in range(M):
            if(can_go(j, k, i)):
                num += 1
                visited[j][k] = True
                dfs(j, k, i)
    # 비교
    if num > max_num:
        max_num = num
        K = i

# 출력
print(K, max_num)