N = int(input())
change_list = [] # 조약돌 바꾸는 과정을 저장하는 리스트
chosen_list = [0] * (4) # 조약돌이 들어있는지 유무 파악 리스트
max_cnt = 0
for i in range(N): # a, b, c 입력
    a, b, c = map(int, input().split())
    change_list.append([a, b, c])

for i in range(1, 4):
    chosen_list[i] = 1
    cnt = 0
    for j in range(N):
        # 조약돌 바꾸기
        chosen_list[change_list[j][0]], chosen_list[change_list[j][1]] = chosen_list[change_list[j][1]], chosen_list[change_list[j][0]]
        # 조약돌이 들어있으면 cnt 1 증가
        if(chosen_list[change_list[j][2]]):
            cnt += 1
    max_cnt = max(max_cnt, cnt)
    # chosen_list 초기화
    chosen_list = [0] * (4)

print(max_cnt)
        
