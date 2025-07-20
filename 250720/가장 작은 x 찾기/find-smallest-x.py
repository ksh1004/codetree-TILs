N = int(input())
num_list = [1] * 11
x2 = 1
for i in range(N):
    a, b = map(int, input().split())
    x2 = x2 * 2
    for j in range(1, 11):
        if(a <= j * x2 and j * x2 <= b):
            continue
        else:
            num_list[j] = 0
min_val = 0
for i in range(1, 11):
    if(num_list[i] == 1):
        min_val = i
        break
print(min_val)