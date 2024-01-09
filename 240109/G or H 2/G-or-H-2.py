N = int(input())
num_list = [0] * 101 # 위치 범위가 0 ~ 100
max_val = 0
for i in range(N): # 위치에 해당하는 정보 입력
    loc, info = input().split()
    loc = int(loc)
    num_list[loc] = info
# 최댓값 찾기
for i in range(101):
    for j in range(i + 1, 101):
        if(num_list[i] == 0 or num_list[j] == 0): # 양끝에 사람이 없는 경우
            continue
        cnt_G = 0
        cnt_H = 0
        for k in range(i, j + 1):
            if(num_list[k] == 'G'):
                cnt_G += 1
            if(num_list[k] == 'H'):
                cnt_H += 1
        if((cnt_G == 0 and cnt_H != 0) or (cnt_G != 0 and cnt_H == 0) or (cnt_G == cnt_H)):
            length = j - i # 길이 계산
            max_val = max(max_val, length)
# 출력
print(max_val)