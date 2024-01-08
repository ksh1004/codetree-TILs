N, S = map(int, input().split())
num_list = list(map(int, input().split()))
val = float('inf') # 가장 가까운 수
temp = 0 # 2개의 수를 제외한 N - 2 개의 수들의 합
for i in range(N): # 첫번째 제외하는 수의 인덱스
    for j in range(i + 1, N): # 두번째 제외하는 수의 인덱스
        temp = 0 # 초기화
        for k in range(N): # 순회
            if(k == i or k == j): # 제외해야 하는 수라면
                continue # 더하지 않고 진행
            else:
                temp += num_list[k]
        # 판단
        if(abs(S - temp) < val): # val 값보다 S - temp의 절댓값이 작으면
            val = abs(S - temp)
# 출력
print(val)