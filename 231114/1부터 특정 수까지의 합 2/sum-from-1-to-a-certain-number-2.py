N = int(input())

def func(num):
    if(num == 1):
        return 1
    
    return func(num - 1) + num

print(func(N))