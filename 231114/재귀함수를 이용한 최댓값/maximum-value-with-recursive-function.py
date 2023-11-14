n = int(input())
num_list = list(map(int, input().split()))

def func(num):
    if(num == 0):
        return num_list[0]
    
    return max(func(num - 1), num_list[num])

print(func(n - 1))