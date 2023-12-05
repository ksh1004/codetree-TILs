N = int(input())
num_list = []
# 격자 채우기
for i in range(N):
    num = list(map(int, input().split()))
    num_list.append(num)
max_cnt = 0 # 최댓값
for i in range(N):
    for j in range(N - 2):
        max_cnt = max(max_cnt, num_list[i][j] + num_list[i][j + 1] + num_list[i][j + 2])
# 출력
print(max_cnt)