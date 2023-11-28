N, K, P, T = map(int, input().split())
# 개발자 수 N, 악수 횟수 K, 감염된 개발자 번호 P, t초동안 하는 악수 횟수 T
num_list = [[0 for _ in range(251)] for _ in range(N + 1)] # 감염 상태 저장
cnt = [K] * (N + 1) # 악수 횟수 저장
# 비감염 0, 감염(전염X) 1, 감염(전염O) 2
info = [] # 악수정보 저장
t_time = [] # 악수하는 시간(초) 저장
for i in range(T):
    t, x, y = map(int, input().split())
    info.append([t, x, y])
    t_time.append(t)
info.sort() # t초 순으로 정렬
for i in range(251):
    # 악수가 시작되기 전이면
    if(i < info[0][0]):
        #print(f'if문: {i}')
        num_list[P][i] = 2 # 최초 감염된 개발자는 전염 가능한 상태로 저장
    # 악수하는 상황이면
    elif(i in t_time):
        #print(f'elif문: {i}')
        for j in range(len(info)):
            if(i == info[j][0]):
                x, y = info[j][1], info[j][2]
        #print(f'x는 {x}, y는{y}')
        # x, y가 아닌 나머지 값들 업데이트
        for j in range(1, N + 1):
            if(j == x or j == y): # 악수 인원은
                pass # pass 후 악수 반영
            else: # 나머지 인원은
                 num_list[j][i] = num_list[j][i - 1] # 지난 정보 가져오기
        # x가 전염이 가능한 상태고 y는 아니라면
        if((num_list[x][i - 1] == 2) and (num_list[y][i - 1] != 2)):
            #print('x가 전염이 가능한 상태고 y는 아니라면')
            cnt[x] -= 1 # 악수 횟수 사용
            # y가 비감염 상태였다면
            if(num_list[y][i - 1] == 0):
                num_list[y][i] = 2 # 전염 정보 저장
            # y가 감염(전염 X) 상태였다면
            elif(num_list[y][i - 1] == 1):
                num_list[y][i] = 1 # 전염 정보 저장
            if(cnt[x] > 0): # x가 전염 가능한 악수 횟수가 남아있으면
                num_list[x][i] = 2 # 여전히 감염(전염 0)
            else: # x가 더이상 전염은 불가하다면
                num_list[x][i] = 1 # 감염(전염 X)로 전환
        # y가 전염이 가능한 상태고 x는 아니라면
        elif((num_list[x][i - 1] != 2) and (num_list[y][i - 1] == 2)):
            #print('y가 전염이 가능한 상태고 x는 아니라면')
            cnt[y] -= 1 # 악수 횟수 사용
            # x가 비감염 상태였다면
            if(num_list[x][i - 1] == 0):
                num_list[x][i] = 2 # 전염 정보 저장
            # x가 감염(전염 X) 상태였다면
            elif(num_list[x][i - 1] == 1):
                num_list[x][i] = 1 # 전염 정보 저장
            if(cnt[y] > 0): # y가 전염 가능한 악수 횟수가 남아있으면
                num_list[y][i] = 2 # 여전히 감염(전염 0)
            else: # y가 더이상 전염은 불가하다면
                num_list[y][i] = 1 # 감염(전염 X)로 전환
        # 둘 다 전염(감염 O) 상태이면
        elif((num_list[x][i - 1] == 2) and (num_list[y][i - 1] == 2)):
            #print('둘 다 전염(감염 O) 상태이면')
            cnt[x] -= 1
            cnt[y] -= 1
            # x, y 상태 업데이트
            if(cnt[x] > 0): # x가 아직 전염이 가능하면
                num_list[x][i] = 2
            else: # x가 더이상 전염은 불가하면
                num_list[x][i] = 1
            if(cnt[y] > 0): # y가 아직 전염이 가능하면
                num_list[y][i] = 2
            else: # y가 더이상 전염은 불가하면
                num_list[y][i] = 1
        # x와 y 둘 다 전염이 안 되는 경우
        else:
            num_list[x][i] = num_list[x][i - 1]
            num_list[y][i] = num_list[y][i - 1]
        #elif(num_list[x][i - 1] <= 1 and num_list[y][i - 1] <= 1):
            #num_list[x][i] = num_list[x][i - 1]
            #num_list[y][i] = num_list[y][i - 1]
    # 악수 하는 상황이 아니라면
    else:
        #print(f'else문: {i}')
        for j in range(1, N + 1):
            #if(j == 1 and i == 8):
                #print(f'num_list[j][i - 1]은: {num_list[j][i-1]}')
            num_list[j][i] = num_list[j][i - 1] # 지난 정보 가져오기
            #if(i == 8):
                #print(f'num_list[j][i]은: {num_list[j][i]}')
# 출력
#print(num_list[1][1:10])
#print(num_list[2][1:10])
#print(num_list[3][1:10])
#print(num_list[4][1:10])
for i in range(1, N + 1):
    if(num_list[i][250] >= 1):
        print(1, end = '')
    else:
        print(0, end = '')