n, m = map(int, input().split())
A, B = [], []
A.append(0)
B.append(0)
# A, B의 이동거리 계산
for i in range(n):
    t, d = input().split()
    t = int(t)
    for j in range(t):
        if(d == 'L'):
            A.append(A[-1] - 1)
        else:
            A.append(A[-1] + 1)
for j in range(m):
    t, d = input().split()
    t = int(t)
    for j in range(t):
        if(d == 'L'):
            B.append(B[-1] - 1)
        else:
            B.append(B[-1] + 1)
# 이동 종료 이후, 다른 로봇이 다 움직일 때까지 같은 위치에 계속 머무르게 저장
if(len(A) >= len(B)): # B는 다 이동했지만 A는 아직 남은 경우
    num = len(A) - len(B)
    for i in range(num):
        B.append(B[-1])
else: # A는 다 이동했지만 B는 아직 남은 경우
    num = len(B) - len(A)
    for i in range(num):
        A.append(A[-1])
# 횟수 계산
cnt = 0
for i in range(1, len(A)):
    if(i == 1): # 첫 번째는 횟수에 포함시키지 않음
        pass
    else:
        # 바로 직전에는 다른 위치에 있다가 그 다음 번에는 같은 위치인 경우
        if((A[i - 1] != B[i - 1]) and (A[i] == B[i])):
            cnt += 1
# 출력
print(cnt)