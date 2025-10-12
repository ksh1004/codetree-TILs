import sys

INT_MAX = sys.maxsize

n = int(input())

max_x1 = 0
min_x2 = INT_MAX

# 시작점 중 가장 뒤에 있는 좌표와 끝점 중 가장 앞에 있는 점의 좌표를 확인합니다.
for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))
    max_x1 = max(max_x1, x1)
    min_x2 = min(min_x2, x2)
    
# 만약 어느 한 선분이라도 시작점이 다른 선분의 끝점보다 뒤에 온다면
# 선분이 전부 겹칠 수 없습니다.
if min_x2 >= max_x1:
    print("Yes")
else:
    print("No")