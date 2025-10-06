n = int(input())
seat = list(input())


def min_dist():
    dist = n
    # 둘 다 1인 곳에 대해
    # 모든 쌍을 조사하여, 그 중 가장 가까운 거리를 구하기
    for i in range(n):
        for j in range(i + 1, n):
            if seat[i] == '1' and seat[j] == '1':
                dist = min(dist, j - i)
    
    return dist


ans = 0
# 들어갈 위치를 일일이 정해보며 그 상황에서 가장 가까운 사람간의 거리를 구해 가능한 경우 중 최댓값을 계산
for i in range(n):
    for j in range(i + 1, n):
        if seat[i] == '0' and seat[j] == '0':
            # 비어있는 위치에 인원을 배치
            seat[i] = seat[j] = '1'
            # 가장 가까운 사람간의 거리를 구해 최댓값을 갱신
            ans = max(ans, min_dist())
            # 다시 채워졌던 값을 되돌려주기
            seat[i] = seat[j] = '0'

print(ans)