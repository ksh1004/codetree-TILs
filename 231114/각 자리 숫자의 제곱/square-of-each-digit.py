N = int(input())

def func(num):
    if(num < 10):
        return num ** 2

    return func(num // 10) + ((num % 10) ** 2)

print(func(N))