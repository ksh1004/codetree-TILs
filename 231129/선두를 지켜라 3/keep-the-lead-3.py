N, M = map(int, input().split())
A, B = [], []
# A의 이동 저장
A.append(0)
for i in range(N):
    v, t = map(int, input().split())
    for j in range(t):
        A.append(A[-1] + v)
# B의 이동 저장
B.append(0)
for i in range(M):
    v, t = map(int, input().split())
    for j in range(t):
        B.append(B[-1] + v)
# 횟수 계산
cnt = 0
val = ''
for i in range(1, len(A)):
    if(i == 1):
        cnt += 1
        if(A[i] >= B[i]):
            val = 'A'
        else:
            val = 'B'
    else:
        if(A[i] >= B[i] and val == 'B'):
            cnt += 1
            val = 'B'
        elif(A[i] < B[i] and val == 'A'):
            cnt += 1
            val = 'A'
# 출력
print(cnt)