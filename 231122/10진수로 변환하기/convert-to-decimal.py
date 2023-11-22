n = input()
bin_list = []
for i in n:
    bin_list.append(int(i))

num = 0
for i in range(len(bin_list)):
    num = num * 2 + bin_list[i]

print(num)

# print(int('0b' + str(n), 2)) # 2진수를 10진수로 변환할 수 있는 int 함수