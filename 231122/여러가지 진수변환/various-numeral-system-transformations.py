N, B = map(int, input().split())
num_list = []
while(True):
    if(N < B):
        num_list.append(N)
        break
    else:
        num = N % B
        num_list.append(num)
        N = N // B

for i in range(len(num_list) - 1, -1, -1):
    print(num_list[i], end = '')