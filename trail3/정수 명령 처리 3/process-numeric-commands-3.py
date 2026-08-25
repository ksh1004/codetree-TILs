n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
from collections import deque
dq = deque()
result = []

for i in range(n):
    c = cmd[i]
    if c == "push_front":
        dq.appendleft(num[i])
    elif c == "push_back":
        dq.append(num[i])
    elif c == "pop_front":
        if dq:
            result.append(dq.popleft())
        else:
            result.append(-1)
    elif c == "pop_back":
        if dq:
            result.append(dq.pop())
        else:
            result.append(-1)
    elif c == "size":
        result.append(len(dq))
    elif c == "empty":
        result.append(1 if not dq else 0)
    elif c == "front":
        if dq:
            result.append(dq[0])
        else:
            result.append(-1)
    elif c == "back":
        if dq:
            result.append(dq[-1])
        else:
            result.append(-1)

print('\n'.join(map(str, result)))