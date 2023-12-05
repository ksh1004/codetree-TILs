A = input() # 문자열 A
cnt = 0 # 횟수
for i in range(len(A)):
    if(A[i] == ')'):
        continue
    for j in range(i + 1, len(A)):
        if(A[j] == ')'):
            cnt += 1
# 출력
print(cnt)