N = int(input())
checkpoint = []
# 체크포인트 좌표 입력
for i in range(N):
    x, y = map(int, input().split())
    checkpoint.append([x, y])
# 최소 거리 계산
min_val = float("inf")
for i in range(1, N - 1): # 1번 체크포인트와 N번 체크포인트 일 때는 제외
    x1, y1 = checkpoint[0][0], checkpoint[0][1] # 1번 체크포인트 기준
    distance_total = 0 # 총 거리
    for j in range(1, N): # 거리 계산 과정
        if(i == j): # 건너뛸 체크포인트 번호일 경우
            continue
        x2, y2 = checkpoint[j][0], checkpoint[j][1]
        distance = abs(x1 - x2) + abs(y1 - y2) # 거리 계산
        distance_total += distance # 거리 추가
        x1, y1 = x2, y2 # 좌표 최신화
    if(distance_total < min_val):
        min_val = distance_total
# 출력
print(min_val)