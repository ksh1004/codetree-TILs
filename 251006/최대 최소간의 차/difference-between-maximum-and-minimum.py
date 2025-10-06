# 입력
n, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()  # 정렬

min_num, max_num = num_list[0], num_list[-1]
diff_need_to_be_modified = (max_num - min_num) - k
if diff_need_to_be_modified <= 0:
    print(0)
    exit()

# 누적합 계산
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + num_list[i]

# get_cost_from_bottom(i) 최적화
def get_cost_from_bottom(num_to_add):
    target = min_num + num_to_add
    import bisect
    idx = 0
    for i, num in enumerate(num_list):
        if num >= target:
            idx = i
            break
    else:
        idx = n
    # idx 이전 값들을 올려야 함
    cost = target * idx - prefix_sum[idx]
    return cost

# get_cost_from_top(j) 최적화
def get_cost_from_top(num_to_minus):
    target = max_num - num_to_minus
    idx = n
    for i in range(n-1, -1, -1):
        if num_list[i] <= target:
            idx = i + 1
            break
    # idx 이후 값들을 내려야 함
    cost = (prefix_sum[n] - prefix_sum[idx]) - target * (n - idx)
    return cost

# 최소 비용 계산
low_cost = float('inf')
for i in range(diff_need_to_be_modified + 1):
    curr_cost = get_cost_from_bottom(i) + get_cost_from_top(diff_need_to_be_modified - i)
    low_cost = min(low_cost, curr_cost)

print(low_cost)