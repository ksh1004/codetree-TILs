import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(N + 1)]

# find 함수
def find(a):
    if(a != arr[a]):
        arr[a] = find(arr[a])
    return arr[a]

def union(a, b):
    r1 = find(a)
    r2 = find(b)
    arr[r1] = r2

for i in range(M):
    num, a, b = map(int, input().split())
    if num == 0:
        union(a, b)
    else:
        if(find(a) == find(b)):
            print(1)
        else:
            print(0)