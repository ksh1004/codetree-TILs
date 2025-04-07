N, C, G, H = map(int, input().split())
ranges = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0
for i in range(0, 1001):
    i_sum = 0
    for j in range(N):
        # Case 1. Ta보다 온도가 낮은 경우
        if(i < ranges[j][0]):
            i_sum += C
        # Case 2. Ta보다 온도가 높거나 같고, Tb보다는 낮거나 같은 경우
        elif(ranges[j][0] <= i and i <= ranges[j][1]):
            i_sum += G
        # Case 3. Tb보다 온도가 높은 경우
        elif(ranges[j][1] < i):
            i_sum += H
    # 값 비교
    max_sum = max(max_sum, i_sum)
# 출력
print(max_sum)