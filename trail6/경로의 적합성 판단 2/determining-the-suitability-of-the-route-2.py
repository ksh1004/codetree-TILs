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
        return
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1

n, m, k = map(int, input().split())

parent = list(range(n + 1))
rank = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

path = list(map(int, input().split()))

ok = True
for i in range(k - 1):
    if find(path[i]) != find(path[i + 1]):
        ok = False
        break

print(1 if ok else 0)