n = int(input())
num_list = list(map(int, input().split()))
mid_list = []
for i in range(n):
    mid_list.append(num_list[i])
    if(i % 2 == 0):
        mid_list.sort()
        print(mid_list[i // 2], end = ' ')