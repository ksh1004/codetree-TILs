N = int(input())

def func(num):
    if(num == 1):
        return 1
    elif(num == 2):
        return 2
    
    return (func(num // 3) + func(num - 1))

print(func(N))