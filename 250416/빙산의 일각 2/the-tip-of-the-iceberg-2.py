n = int(input())
h = [int(input()) for _ in range(n)]

max_cnt = 0
for i in range(1, 1001):
    cnt = 0
    prev_val = 0 # 0이면 잠긴 상태, 1이면 안 잠긴 상태
    for j in range(len(h)):
        if j == 0: # 첫 번째 빙산
            if(h[j] > i): # 안 잠기면
                prev_val = 1 # 값을 1로
                cnt += 1
        else:
            if(h[j] > i): # 안 잠기면
                if(prev_val == 0): # 이전 값은 잠긴 상태였다면
                    prev_val = 1
                    cnt += 1
                else:
                    continue
            else:
                prev_val = 0
    max_cnt = max(max_cnt, cnt)

print(max_cnt)