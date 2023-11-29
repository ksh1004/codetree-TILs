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
    if(i == 1): # 첫 번째의 경우
        cnt += 1 # 첫 번째 명예의 전당도 횟수에 포함
        if(A[i] > B[i]): # A가 B보다 클 때
            val = 'A'
        elif(A[i] < B[i]): # B가 A보다 클 때
            val = 'B'
        else: # A와 B가 같을 때
            val = 'AB'
    else:
        if(A[i] > B[i]): # A가 B보다 클 때
            if(val != 'A'):
                cnt += 1
                val = 'A'
        elif(A[i] < B[i]): # B가 A보다 클 때
            if(val != 'B'):
                cnt += 1
                val = 'B'
        else:
            if(val != 'AB'): # A와 B가 같을 때
                cnt += 1
                val = 'AB'
# 출력
print(cnt)