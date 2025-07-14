N, M = map(int, input().split())
num_list = list(map(int, input().split()))
max_val = -1
for i in range(1, N + 1): # 시작 위치는 1부터 N까지 숫자
    val = 0 # 값 비교를 위한 변수
    position = i - 1 # 위치값
    for j in range(M): # 움직임 구현
        val += num_list[position]
        position = num_list[position] - 1
    # 값 비교
    max_val = max(max_val, val)
# 출력
print(max_val)