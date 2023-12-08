N, M = map(int, input().split())
arr = []
# 문자열 격자 삽입
for i in range(N):
    s = input()
    arr.append(s)
# 범위함수
def in_range(x, y):
    return (0 <= x and x < N and 0 <= y and y < M)
# 북, 북서, 서, 남서, 남, 남동, 동, 북동
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
cnt = 0
# 탐색
for i in range(N):
    for j in range(M):
        if(arr[i][j] != 'L'): # L이 아니면
            continue
        # L이면 탐색 시작
        for k in range(8):
            idx = 1
            cur_x = i
            cur_y = j
            while True:
                nx = cur_x + dx[k]
                ny = cur_y + dy[k]
                if(in_range(nx, ny) == False): # 격자 범위를 벗어나면
                    break
                if(arr[nx][ny] != 'E'): # E가 아니면
                    break
                idx += 1 # 횟수 증가
                # 좌표 최신화
                cur_x = nx
                cur_y = ny
                if(idx == 3): # 'LEE'가 완성되면
                    cnt += 1
                    break
# 출력
print(cnt)