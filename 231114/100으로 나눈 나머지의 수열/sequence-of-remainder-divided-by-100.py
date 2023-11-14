N = int(input())

def func(num):
    if(num == 1):
        return 2
    elif(num == 2):
        return 4
    
    return (func(num - 1) * func(num - 2)) % 100

print(func(N))