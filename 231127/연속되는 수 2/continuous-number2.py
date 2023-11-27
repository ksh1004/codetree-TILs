N = int(input())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)
num_list.sort()
max_val = 0 # 횟수 최댓값
val = 0 # 숫자값
cnt = 0 # 횟수를 세는 변수
# 연속 숫자 횟수 최댓값 구하기
for i in range(len(num_list)):
    if(i == 0): # 첫번째는 예외처리
        val = num_list[i]
        cnt += 1
        if(i == len(num_list) - 1): # 만약 현재 값이 마지막 값이라면
                if(max_val < cnt): # 현재의 횟수값이 max 값보다 크다면
                    max_val = cnt # 현재값을 max 값으로
    else:
        if(num_list[i] == val): # 만약 직전 값과 현재 값이 동일한 숫자이면
            cnt += 1 # 횟수 1 증가
            if(i == len(num_list) - 1): # 만약 현재 값이 마지막 값이라면
                if(max_val < cnt): # 현재의 횟수값이 max 값보다 크다면
                    max_val = cnt # 현재값을 max 값으로
        else:  # 만약 직전 값과 현재 값과 다른 숫자이면
            if(max_val < cnt): # 현재의 횟수값이 max 값보다 크다면
                max_val = cnt # 현재값을 max 값으로
            cnt = 1 # 횟수 초기화
            val = num_list[i] # 숫자값 최신화
# 출력
print(max_val)