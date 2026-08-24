N, M = map(int, input().split()) # 정점 갯수 N, 간선 갯수 M
gp = [[] for _ in range(N + 1)] # 정점 및 간선 정보 저장 그래프
for i in range(M): # 간선 삽입
    a, b = map(int, input().split())
    gp[a].append(b)
    gp[b].append(a)

visits = [0 for _ in range(N + 1)] # 방문 여부 판별
def dfs(v):
    visits[v] = 1 # 해당 정점 방문
    cnt = 1 # 정점 연결 갯수
    for i in gp[v]: # 연결된 정점 중
        if(visits[i] == 0): # 아직 방문 안했으면
            cnt += dfs(i) # dfs 수행
    return cnt

result = dfs(1) - 1 # 탐색 수행(본인 정점은 제외)
print(result) # 출력