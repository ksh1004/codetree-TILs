N, H, T = map(int, input().split())
num_list = list(map(int, input().split()))
min_val = 999999999
# 최소 비용 계산
for i in range(N - T + 1):
    temp = 0
    for j in range(i, i + T):
        temp += abs(num_list[j] - H)
    min_val = min(min_val, temp)
# 출력
print(min_val)