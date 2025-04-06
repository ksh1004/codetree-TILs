N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

max_num = -1
for i in range(N):
    # 거리를 정하기 위한 값
    min_cnt = max(0, i - K) # 좌측 끝
    max_cnt = min(N, i + K) # 우측 끝
    for j in range(min_cnt, max_cnt):
        if(i == j):
            continue
        if(num[j] == num[i]):
            max_num = max(max_num, num[j])

# 출력
print(max_num)