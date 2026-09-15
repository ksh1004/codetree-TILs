n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

parent = list(range(n + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    parent[rb] = ra
    return True

edges.sort(key=lambda x: x[2])

total = cnt = 0
for u, v, w in edges:
    if union(u, v):
        total += w
        cnt += 1
        if cnt == n - 1:
            break

print(total)