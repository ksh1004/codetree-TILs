cnt = [0] * 200001 # 색칠 없음: 0, 흰색: 1, 검은색: 2, 회색: 3
cnt_white = [0] * 200001 # 흰색 덧칠 횟수
cnt_black = [0] * 200001 # 검은색 덧칠 횟수
n = int(input())
idx = 100000 # 시작 인덱스
for i in range(n):
    num, order = input().split()
    num = int(num)
    if(order == 'L'):
        for i in range(idx, idx - num, -1):
            cnt_white[i] += 1 # 흰색 덧칠 횟수 1 증가
            if((cnt_white[i] >= 2 and cnt_black[i] >= 2) or cnt[i] == 3): # 흰색과 검은색 둘다 2번 이상 칠하면
                cnt[i] = 3 # 회색으로 덧칠
            else:
                cnt[i] = 1 # 흰색으로 칠함
        idx = (idx - num + 1)
    else:
        for i in range(idx, idx + num):
            cnt_black[i] += 1 # 검은색 덧칠 횟수 1 증가
            if((cnt_white[i] >= 2 and cnt_black[i] >= 2) or cnt[i] == 3): # 흰색과 검은색 둘다 2번 이상 칠하면
                cnt[i] = 3 # 회색으로 덧칠
            else:
                cnt[i] = 2 # 검은색으로 칠함
        idx = (idx + num - 1)

total_white = 0
total_black = 0
total_gray = 0
for i in range(len(cnt)):
    if(cnt[i] == 1):
        total_white += 1
    elif(cnt[i] == 2):
        total_black += 1
    elif(cnt[i] == 3):
        total_gray += 1
print(total_white, total_black, total_gray)