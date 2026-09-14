n, m = map(int, input().split())
type_arr = input().split()
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

# 종류가 다른 간선만 남기고 가중치 오름차순 정렬
cand = [e for e in edges if type_arr[e[0] - 1] != type_arr[e[1] - 1]]
cand.sort(key=lambda x: x[2])

total = cnt = 0
for u, v, w in cand:
    if union(u, v):
        total += w
        cnt += 1
        if cnt == n - 1:
            break

print(total if cnt == n - 1 else -1)