N = input()
# 2진수 값 저장
bin_list = []
for i in N:
    bin_list.append(int(i))
# 2진수를 10진수로 변환
num = 0
for i in range(len(bin_list)):
    num = num * 2 + bin_list[i]
# 10진수 값에 17배
num = num * 17
# 10진수를 2진수로 변환
bin_list = []
while(True):
    if(num < 2):
        bin_list.append(num)
        break
    else:
        n = num % 2
        bin_list.append(n)
        num = num // 2
# 2진수 값 출력
for i in range(len(bin_list) - 1, -1, -1):
    print(bin_list[i], end = '')