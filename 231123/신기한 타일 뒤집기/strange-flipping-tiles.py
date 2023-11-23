cnt = [0] * 200001 # 회색: 0, 흰색: 1, 검은색: 2
n = int(input())
idx = 100000 # 시작 인덱스
for i in range(n):
    num, order = input().split()
    num = int(num)
    if(order == 'L'):
        for i in range(idx, idx - num, -1):
            cnt[i] = 1 # 흰색으로 칠함
        idx = (idx - num + 1)
    else:
        for i in range(idx, idx + num):
            cnt[i] = 2 # 검은색으로 칠함
        idx = (idx + num - 1)

total_white = 0
total_black = 0
for i in range(len(cnt)):
    if(cnt[i] == 1):
        total_white += 1
    elif(cnt[i] == 2):
        total_black += 1
print(total_white, total_black)