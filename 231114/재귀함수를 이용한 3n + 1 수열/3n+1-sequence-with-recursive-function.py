n = int(input())

def func(num):
    if(num == 1):
        return 0
    
    if(num % 2 == 0):
        return func(num // 2) + 1
    else:
        return func(num * 3 + 1) + 1

print(func(n))