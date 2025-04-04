K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]

cnt = 0
for i in range(1, N + 1): # 첫 번째 개발자 i
    for j in range(1, N + 1): # 두 번째 개발자 j
        if(i == j):
            continue
        check_num = 1 # 항상 우선순위가 앞서있는지 확인
        for k in range(K):
            if(arr[k].index(i) < arr[k].index(j)): # i 개발자가 j 개발자보다 우선인지
                continue
            else: # j 개발자가 i 개발자보다 우선순위가 있는 경우
                check_num = 0 # 항상 우선순위가 앞서있지는 않음
                break
        if(check_num):
            cnt += 1

print(cnt)