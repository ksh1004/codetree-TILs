n = int(input())
num_list = []
while(True):
    if(n < 2):
        num_list.append(n)
        break
    else:
        num = n % 2
        num_list.append(num)
        n = n // 2

for i in range(len(num_list) - 1, -1, -1):
    print(num_list[i], end = '')

# print(bin(n)[2:]) # 10진수를 2진수로 변환해주는 bin() 내장함수