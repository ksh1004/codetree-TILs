import sys
# 알이 놓이지 않는 자리 0, 검은알 1, 흰알 2
num_list = [list(map(int, input().split())) for _ in range(19)] # 오목판 정보 입력
# 범위 함수
def in_range(x, y):
    return (0 <= x and x < 19 and 0 <= y and y < 19)
# 이동 방향(서남, 남, 남동, 동, 북동, 북, 북서, 서)
dx, dy = [1, 1, 1, -1, -1, -1, 0, 0], [-1, 0, 1, -1, 0, 1, -1, 1]
# 좌표에서 확인
for i in range(19):
    for j in range(19):
        if(num_list[i][j] == 0): # 바둑 알이 없다면
            continue

        for k in range(8):
            cnt = 1
            cur_x = i # 현재 x
            cur_y = j # 현재 y
            while True:
                nx = cur_x + dx[k]
                ny = cur_y + dy[k]
                if(in_range(nx, ny) == False): # 범위를 벗어나면
                    break
                if(num_list[nx][ny] != num_list[cur_x][cur_y]): # 바둑알이 다르면
                    break
                cnt += 1
                cur_x = nx
                cur_y = ny
                if(cnt == 5): # 오목이 완성되면
                    print(num_list[i][j])
                    print(i + 2 * dx[k] + 1, j + 2 * dy[k] + 1)
                    sys.exit()
print(0)