N = int(input())
num_list = list(map(float, input().split()))
cnt = 0 # 횟수
for i in range(N): # 구간의 시작 인덱스
    for j in range(i, N): # 구간의 끝 인덱스
        temp = 0 # 현재 구간 합
        temp_cnt = 0 # 구간의 크기
        for k in range(i, j + 1):
            temp = num_list[k] # 구간 값 추가
            temp_cnt += 1 # 크기 1 증가
        temp_avg = temp / temp_cnt # 구간의 평균값
        for k in range(i, j + 1):
            if(temp_avg == num_list[k]): # 구간 평균값이 구간 내 원소값과 동일하면
                cnt += 1 # 횟수 1 증가
                break
# 출력
print(cnt)