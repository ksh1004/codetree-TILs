N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
from collections import deque
queue = deque()
result = []

for i in range(N):
    cmd = command[i]
    if cmd == "push":
        queue.append(A[i])
    elif cmd == "pop":
        if queue:
            result.append(queue.popleft())
        else:
            result.append(-1)
    elif cmd == "size":
        result.append(len(queue))
    elif cmd == "empty":
        result.append(1 if not queue else 0)
    elif cmd == "front":
        if queue:
            result.append(queue[0])
        else:
            result.append(-1)

print('\n'.join(map(str, result)))