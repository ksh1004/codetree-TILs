N, M = map(int, input().split())
num_list = [[0 for _ in range(N + 1)] for _ in range(N + 1)] # N * N 격자
# 격자에서는 x가 행, y가 열이고, 남북 이동시 x가 1, -1만큼 변화, 동서 이동시 y가 1, -1만큼 변화
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1] # 북, 서, 남, 동
# 격자 색칠 및 편안한 상태(인접 칸이 칠해진 갯수가 정확히 3개)인지 확인
for i in range(M):
    r, c = map(int, input().split())
    num_list[r][c] = 1
    cnt = 0
    for j in range(4):
        nx, ny = r + dx[j], c + dy[j]
        if(nx >= 1 and nx <= N and ny >= 1 and ny <= N): # 격자 안에 들어오는 경우
            if(num_list[nx][ny] == 1): # 격자가 칠해져 있다면
                cnt += 1 # cnt 1 증가
    if(cnt == 3): # 인접한 칠해진 격자가 총 3개면
        print(1)
    else:
        print(0)