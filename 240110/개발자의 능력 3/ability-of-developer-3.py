num_list = list(map(int, input().split())) # 6명의 개발자 능력값 리스트
sum_val = sum(num_list) # 리스트의 총합
min_val = float('inf') # 최솟값
# 최솟값 계산
for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            sum1 = num_list[i] + num_list[j] + num_list[k]
            sum2 = sum_val - sum1
            diff = abs(sum1 - sum2)
            if(diff < min_val):
                min_val = diff
# 출력
print(min_val)