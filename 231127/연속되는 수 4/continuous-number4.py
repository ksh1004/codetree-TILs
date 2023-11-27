N = int(input())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)
max_val = 0
cnt = 0
for i in range(len(num_list)):
    if(i == 0): # 첫 번째 숫자이면
        cnt = 1
        if(N == 1): # 1개의 숫자만 주어지면(즉, N이 1일 때)
            max_val = cnt
    else:
        last = num_list[i - 1] # 직전값
        now = num_list[i] # 현재값
        if(last < now): # 증가하는 경우
            cnt += 1
            if(i == len(num_list) - 1): # 마지막일 때
                max_val = max(cnt, max_val)
        else: # 증가하지 않는 경우
            max_val = max(cnt, max_val)
            cnt = 1
# 출력
print(max_val)