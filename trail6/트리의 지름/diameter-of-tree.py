from collections import deque, defaultdict

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

graph = defaultdict(list)
for a, b, w in edges:
    graph[a].append((b, w))
    graph[b].append((a, w))

def bfs(start):
    dist = {start: 0}
    q = deque([start])
    farthest_node = start
    max_dist = 0
    while q:
        cur = q.popleft()
        for nxt, w in graph[cur]:
            if nxt not in dist:
                dist[nxt] = dist[cur] + w
                if dist[nxt] > max_dist:
                    max_dist = dist[nxt]
                    farthest_node = nxt
                q.append(nxt)
    return farthest_node, max_dist

# 1) 임의의 노드(1번)에서 가장 먼 노드 A를 찾음
node_a, _ = bfs(1)
# 2) A에서 가장 먼 노드까지의 거리가 트리의 지름
_, diameter = bfs(node_a)

print(diameter)