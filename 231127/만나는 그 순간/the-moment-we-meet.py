N, M = map(int, input().split())
A, B = [], []
# A 이동
A.append(0) # 시작점 삽입
for i in range(1, N + 1):
    d, t = input().split()
    t = int(t)
    if(d == 'R'): # 오른쪽으로 이동할 경우
        for j in range(t):
            num = A[-1] + 1
            A.append(num)
    else: # 왼쪽으로 이동할 경우
        for j in range(t):
            num = A[-1] - 1
            A.append(num)
# B 이동
B.append(0) # 시작점 삽입
for i in range(1, M + 1):
    d, t = input().split()
    t = int(t)
    if(d == 'R'): # 오른쪽으로 이동할 경우
        for j in range(t):
            num = B[-1] + 1
            B.append(num)
    else: # 왼쪽으로 이동할 경우
        for j in range(t):
            num = B[-1] - 1
            B.append(num)
idx = -1 # 최초로 만나는 인덱스
for i in range(1, len(A)):
    if(A[i] == B[i]): # 만약 최초로 만나는 경우
        idx = i # 해당 인덱스 저장
        break
# 출력
print(idx)