n, k = map(int, input().split())

# Please write your code here.
from collections import deque

queue = deque(range(1, n + 1))
result = []

while queue:
    queue.rotate(-(k - 1))
    result.append(queue.popleft())

print(' '.join(map(str, result)))