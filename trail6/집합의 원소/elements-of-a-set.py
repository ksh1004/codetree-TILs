import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 압축 (경로 절반 압축)
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    # union by rank
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]:
        rank[ra] += 1

n, m = map(int, input().split())
parent = list(range(n + 1))
rank = [0] * (n + 1)

result = []
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:
        result.append('1' if find(a) == find(b) else '0')

print('\n'.join(result))