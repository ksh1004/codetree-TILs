N, K = map(int, input().split())
num_list = [0] * 10001
for i in range(N): # 배열에 값 기록
    loc, info = input().split()
    loc = int(loc)
    if(info == 'G'):
        num_list[loc] = 1
    elif(info == 'H'):
        num_list[loc] = 2
# 최댓값 계산
max_val = -1
for i in range(1, 10001 - K): # 1부터 10001 - K + 1 까지
    temp = 0
    for j in range(i, i + K + 1): # i부터 i + K 까지 합산
        temp += num_list[j]
    if(max_val < temp):
        max_val = temp
# 출력
print(max_val)