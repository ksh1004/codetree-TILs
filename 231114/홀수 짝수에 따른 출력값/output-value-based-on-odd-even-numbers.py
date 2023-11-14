N = int(input())

def func(num):
    if(num % 2 == 0):
        if(num == 2):
            return 2
        return func(num - 2) + num
    else:
        if(num == 1):
            return 1
        return func(num - 2) + num

print(func(N))