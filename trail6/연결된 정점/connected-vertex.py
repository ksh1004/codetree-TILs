N, M = map(int, input().split())
arr = [i for i in range(N + 1)]
size = [1 for i in range(N + 1)]

def find(x):
    if(x != arr[x]):
        arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    r1 = find(x)
    r2 = find(y)

    if r1 == r2:
        return

    if(size[r1] < size[r2]):
        r1, r2 = r2, r1

    arr[r2] = r1
    size[r1] += size[r2]

for _ in range(M):
    li = input().split()

    if li[0] == 'x':
        a, b = int(li[1]), int(li[2])
        union(a, b)

    else:
        val = int(li[1])
        root = find(val)
        print(size[root])