N = int(input())   # 격자의 크기
grid = [list(map(int, input().split())) for _ in range(N)]   # 격자의 정보

max_cnt = -1 # 최대 동전 갯수
for i in range(0, N-2): # i : 3 x 3 행의 시작점
    for j in range(0, N-2): # j : 3 x 3 열의 시작점
        cnt = 0 # 3 x 3에서의 동전 개수 카운팅
        for k in range(i, i + 3): # 3 x 3 격자 탐색
            for l in range(j, j + 3):
                if(grid[k][l] == 1): # 격자 안에 동전(1)이 있다면
                    cnt += 1 # 카운트 증가
        # 최대 동전 개수와 비교하여 현재 동전 개수가 더 많으면 최신화
        max_cnt = max(max_cnt, cnt)
# 출력
print(max_cnt)    