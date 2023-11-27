N = int(input())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)
# 연속 부분 수열 구하기
max_val = 0 # 최대 길이
cnt = 0 # 길이
for i in range(len(num_list)):
    if(i == 0): # 첫 번째 경우
        cnt += 1
        if(N == 1): # N 값이 1로 주어지면
            max_val = cnt
    else: # 첫 번째가 아닌 경우
        last = num_list[i - 1] # 직전값
        now = num_list[i] # 현재값
        if((last < 0 and now < 0) or (last > 0 and now > 0)): # 같은 부호가 연속되면
            cnt += 1
            if(i == len(num_list) - 1):
                if(max_val < cnt):
                    max_val = cnt
        else: # 연속이 아닌 경우
            if(max_val < cnt):
                max_val = cnt
            cnt = 1
# 출력
print(max_val)