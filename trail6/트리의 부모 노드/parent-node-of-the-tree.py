n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
visited = [False] * (n + 1)

# BFS로 루트(1)부터 탐색하며 부모 지정
from collections import deque

queue = deque([1])
visited[1] = True

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = cur
            queue.append(nxt)

# 2번 노드부터 N번 노드까지 부모 출력
for i in range(2, n + 1):
    print(parent[i])