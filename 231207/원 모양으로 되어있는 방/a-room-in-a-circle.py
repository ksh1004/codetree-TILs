N = int(input())
num_list = []
# 인원 입력받기
for i in range(N):
    num = int(input())
    num_list.append(num)
# 최솟값 계산
min_val = float('inf')
for i in range(N):
    distance_total = 0 # 총합 이동거리
    distance_val = 0 # 방 사이 이동거리
    for j in range(i, i + N):
        idx = (j) % N # 해당 인덱스
        distance = num_list[idx] * distance_val # 이동거리 계산
        distance_total += distance # 총합에 추가
        distance_val += 1
    if(distance_total < min_val):
        min_val = distance_total
# 출력
print(min_val)