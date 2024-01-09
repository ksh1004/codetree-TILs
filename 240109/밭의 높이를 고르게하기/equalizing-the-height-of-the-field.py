N, H, T = map(int, input().split())
num_list = list(map(int, input().split()))
min_val = float('inf')
# 최소 비용 계산
for i in range(N - T + 1):
    temp = 0
    for j in range(i, i + T):
        temp += abs(j - H)
    if(temp < min_val):
        min_val = temp
# 출력
print(min_val)