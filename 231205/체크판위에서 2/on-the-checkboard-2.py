R, C = map(int, input().split())
str_list = []
# 격자 삽입
for i in range(R):
    s = list(input().split())
    str_list.append(s)
cnt = 0
# 왼쪽 상단에서 출발, 오른쪽 하단에 도착
for i in range(1,  R): # 첫 번째 하단 이동 계산
    for j in range(1, C): # 첫 번째 우측 이동 계산
        for k in range(i + 1, R - 1): # 두 번째 하단 이동 계산
            for l in range(j + 1, C - 1): # 두 번째 우측 이동 계산
                if(str_list[0][0] != str_list[i][j] and \
                str_list[i][j] != str_list[k][l] and \
                str_list[k][l] != str_list[R - 1][C - 1]):
                    cnt += 1
# 출력
print(cnt)