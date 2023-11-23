n = int(input())
cnt = [0] * 201
cnt[100] += 1 # -100 ~ 100에서 0 ~ 200으로 계산하고, 위치 0 -> 100에서 시작하므로 해당 위치에 1 증가
idx = 100 # 시작 인덱스
for i in range(n):
    num, order = input().split()
    num = int(num)
    if(order == 'L'):
        for j in range(idx, idx - num, -1):
            cnt[j] += 1
        idx = idx - num
    else:
        for j in range(idx, idx + num):
            cnt[j] += 1
        idx = idx + num
total = 0
for i in range(len(cnt)):
    if(cnt[i] >= 2):
        total += 1
print(total)