n = int(input())

# Please write your code here.
from collections import deque

dq = deque(range(1, n + 1))

while len(dq) > 1:
    dq.popleft()              # 맨 앞 제거
    dq.append(dq.popleft())   # 남은 맨 앞을 뒤로 이동

print(dq[0])