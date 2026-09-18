from collections import deque

n, m = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

# 그래프 생성
for a, b in edges:
    graph[a].append(b)
    indegree[b] += 1

# 진입 차수가 0인 친구를 큐에 삽입
q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

answer = []

# 위상 정렬
while q:
    cur = q.popleft()
    answer.append(cur)

    for nxt in graph[cur]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

print(*answer)