n = int(input())
num_list = []
# 격자 입력받기
for i in range(n):
    num = list(map(int, input().split()))
    num_list.append(num)
# 개수 세기
cnt = 0 # 개수 변수
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 북, 서, 남, 동 순서
for i in range(n):
    for j in range(n):
        x, y = i, j
        count = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if(nx >= 0 and nx < n and ny >= 0 and ny < n): # 인접 칸이 격자 안에 들어오면
                if(num_list[nx][ny] == 1):
                    count += 1
        if(count >= 3):
            cnt += 1
# 출력
print(cnt)