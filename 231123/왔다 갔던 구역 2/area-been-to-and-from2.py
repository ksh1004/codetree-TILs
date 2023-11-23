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
idx = -1 # 인덱스 변수 재활용
for i in range(len(cnt)):
    if(cnt[i] >= 2): # 만약 2번 이상 지나간 영역이면
        if(idx == -1): # 근데 구간 설정이 안되어있으면
            idx = i # 구간 설정
    else: # 2번 미만으로 지나간 영역이면
        if(idx != -1): # 이전에 2번 이상 지나간 구간이 있는 경우
            total += (i - idx) # 해당 구간을 더한다(i - 1로 하는 이유는, 현재 i값은 2번 이상 이어진 것이 아니고, 직전 i값까지 이어진 것이기 때문)
            idx = -1
print(total)