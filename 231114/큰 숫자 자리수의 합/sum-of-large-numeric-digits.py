num_list = list(map(int, input().split()))
N = num_list[0] * num_list[1] * num_list[2]

def func(num):
    if(num < 10):
        return num
    
    return func(num // 10) + (num % 10)

print(func(N))