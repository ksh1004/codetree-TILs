n = int(input())
num_list = list(map(int, input().split()))
max_val = -1
# 최댓값 계산
for i in range(0, n - 2):
    for j in range(i + 2, n):
        sum_val = num_list[i] + num_list[j]
        if(max_val < sum_val):
            max_val = sum_val
# 출력
print(max_val)