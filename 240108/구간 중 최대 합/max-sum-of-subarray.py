n, k = map(int, input().split())
num_list = list(map(int, input().split()))
max_val = -1
for i in range(n - k + 1): # 0 부터 n - k 까지
    temp = 0
    for j in range(i, i + k): # 연속하는 k개의 숫자 합산
        temp += num_list[j]
    if(max_val < temp): # 기존의 최댓값보다 크면
        max_val = temp # 현재 값으로 최댓값 변경
# 출력
print(max_val)