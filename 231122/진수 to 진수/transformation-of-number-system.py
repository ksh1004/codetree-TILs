a, b = map(int, input().split())
n = input()
# a진수 값 저장
num_list = []
for i in n:
    num_list.append(int(i))
# a진수를 10진수로 변환
num = 0
for i in range(len(num_list)):
    num = num * a + num_list[i]
# 10진수를 b진수로 변환
bin_list = []
while(True):
    if(num < b):
        bin_list.append(num)
        break
    else:
        n = num % b
        bin_list.append(n)
        num = num // b
# b진수 값 출력
for i in range(len(bin_list) - 1, -1, -1):
    print(bin_list[i], end = '')