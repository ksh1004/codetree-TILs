N = int(input())
num_list = list(map(int, input().split()))
min_total = float('inf') # 최솟값

for i in range(N):
    num_list[i] = num_list[i] * 2 # 하나의 숫자에 2배
    now_total = 0
    for j in range(N):
        temp = num_list[j]
        del num_list[j] # 하나의 숫자를 제거
        for k in range(1, len(num_list)):
            val = abs(num_list[k] - num_list[k - 1])
            now_total += val
        min_total = min(min_total, now_total) # 최솟값 업데이트
        num_list.insert(j, temp) # 제거했던 값 원상복구
    num_list[i] = num_list[i] // 2 # 2배했던 값 원상복구

print(min_total) # 출력