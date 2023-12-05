N = input()
max_val = -1
# 시뮬레이션
for i in range(len(N)):
    if(N[i] == '1'): # 1이면
        num = '0b' + N[:i] + '0' + N[i + 1:] # 0으로
        num = int(num, 2) # 2진수 변환
        if(max_val < num):
            max_val = num
    else:
        num = '0b' + N[:i] + '1' + N[i + 1:] # 0으로
        num = int(num, 2) # 2진수 변환
        if(max_val < num):
            max_val = num
# 출력
print(max_val)