import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1
    return True

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

parent = list(range(n + 1))
rank = [0] * (n + 1)

edges.sort(key=lambda e: e[2])

total = 0
for a, b, w in edges:
    if union(a, b):
        total += w

print(total)