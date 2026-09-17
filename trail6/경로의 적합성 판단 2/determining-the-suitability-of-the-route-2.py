import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [i for i in range(n + 1)]

def find(x):
    if(x != arr[x]):
        arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    r1 = find(x)
    r2 = find(y)
    arr[r1] = r2

for i in range(m):
    num1, num2 = map(int, input().split())
    union(num1, num2)

point = list(map(int, input().split()))
check = 1
for i in range(1, len(point)):
    if(find(point[i]) != find(point[i - 1])):
        check = 0

print(check)