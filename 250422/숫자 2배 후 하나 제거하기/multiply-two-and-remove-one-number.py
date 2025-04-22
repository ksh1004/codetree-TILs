N = int(input())
num_list = list(map(int, input().split()))
min_total = float('inf')

for i in range(N):
    # i번째 값을 2배로 만든 새로운 리스트
    doubled_list = num_list[:]
    doubled_list[i] *= 2

    for j in range(N):
        # j번째 값을 제거
        if i == j:
            continue  # 같은 인덱스를 제거하는 건 무의미하므로 스킵

        temp_list = doubled_list[:j] + doubled_list[j+1:]

        now_total = 0
        for k in range(1, len(temp_list)):
            now_total += abs(temp_list[k] - temp_list[k - 1])

        min_total = min(min_total, now_total)

print(min_total)
