N, M = map(int, input().split())
A, B = [], []
# A의 이동 계산
A.append(0)
for i in range(N):
    v, t = map(int, input().split())
    for j in range(t):
        A.append(A[-1] + v)
# B의 이동 계산
B.append(0)
for i in range(M):
    v, t = map(int, input().split())
    for j in range(t):
        B.append(B[-1] + v)
# 선두 횟수 계산
cnt = 0 # 선두 횟수 저장
val = '' # 선두를 나타내는 변수
for i in range(1, len(A)):
    if(i == 1):
        if(A[i] >= B[i]): # A가 선두이면
            val = 'A'
        else:
            val = 'B'
    else:
        if(A[i] >= B[i]): # A가 선두일 때
            if(val != 'A'): # B가 선두였는데 A로 바뀌었으면
                cnt += 1 # 선두 변경 횟수 증가
                val = 'A' # 선두 변수 변경
        else: # B가 선두일 때
            if(val != 'B'): # A가 선두였는데 B로 바뀌었으면
                cnt += 1 # 선두 변경 횟수 증가
                val = 'B' # 선두 변수 변경
# 출력
print(cnt)