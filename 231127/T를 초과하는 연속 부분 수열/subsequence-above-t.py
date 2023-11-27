n, t = map(int, input().split())
num_list = list(map(int, input().split()))
max_val = 0
cnt = 0
for i in range(len(num_list)):
    if(i == 0): # 첫 번째 숫자이면
        if(num_list[i] > t):
            cnt += 1
        if(n == 1): # 1개의 숫자만 주어지면(즉, N이 1일 때)
            max_val = cnt
    else:
        if(num_list[i] > t): # 현재 값이 t보다 큰 경우
            cnt += 1
            if(i == len(num_list) - 1): # 마지막일 때
                max_val = max(cnt, max_val)
        else: # 현재 값이 t보다 크지 않은 경우
            max_val = max(cnt, max_val)
            cnt = 0
# 출력
print(max_val)