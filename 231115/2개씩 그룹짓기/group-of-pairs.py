N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
max_sum = -1

for i in range(N):
    num1 = num_list[i]
    num2 = num_list[2 * N - (i + 1)]
    if(num1 + num2 > max_sum):
        max_sum = num1 + num2

print(max_sum)