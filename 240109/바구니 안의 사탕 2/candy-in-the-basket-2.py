N, K = map(int, input().split())
num_list = [0] * 101 # 바구니 위치 범위가 0 ~ 100
for i in range(N): # 사탕 갯수와 바구니 좌표 입력
    cnt, loc = map(int, input().split())
    num_list[loc] += cnt
max_val = -1 # 최댓값
# 최댓값 계산
for i in range(K, 100 - K): # K 부터 100 - K 까지
    temp = 0 # 현재 구간의 사탕 갯수
    for j in range(i - K, i + K + 1):
        temp += num_list[j]
    if(max_val < temp): # 기존 최댓값보다 현재 값이 더 크면
        max_val = temp # 최댓값 변경
# 출력
print(max_val)