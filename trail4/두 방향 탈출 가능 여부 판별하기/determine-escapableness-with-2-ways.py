N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] # 그래프

start = (0, 0) # 시작 지점
end = (N - 1, M - 1) # 끝 지점

memo = [[-1] * M for _ in range(N)] # DP

def dfs(v):
    x, y = v # 시작 지점의 x좌표, y좌표 설정
    check = 0 # 경로 존재 여부를 판단할 변수
    # 오른쪽과 아래로만 이동
    dx = [0, 1] # x축 이동
    dy = [1, 0] # y축 이동

    if(v == end): # 끝 지점에 도달할 경우
        check = 1 # 경로가 있다고 판단
        return check

    if memo[x][y] != -1: # 이미 계산된 적이 있으면
        return memo[x][y] # 바로 값 반환
    
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i] # 이동할 좌표 값
        if(0 <= nx < N) and (0 <= ny < M): # 격자 범위 안에 있는 경우
            if(arr[nx][ny] == 1): # 이동 가능한 경우
                check = check or dfs((nx, ny)) # DFS 수행
                if check:
                    break
    
    memo[x][y] = check # 계산 결과 저장
    return check

result = dfs(start)
print(result)