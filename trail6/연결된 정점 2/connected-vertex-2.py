n = int(input())

edges = [tuple(map(int, input().split())) for _ in range(n)]

parent = {}
size = {}


def find(x):
    # 처음 등장한 정점
    if x not in parent:
        parent[x] = x
        size[x] = 1
        return x

    # 경로 압축
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    # 이미 같은 연결 컴포넌트
    if root_a == root_b:
        return size[root_a]

    # 큰 컴포넌트 아래에 작은 컴포넌트를 합침
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a
    size[root_a] += size[root_b]

    return size[root_a]


for a, b in edges:
    print(union(a, b))