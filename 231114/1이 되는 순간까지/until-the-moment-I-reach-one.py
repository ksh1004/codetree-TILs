N = int(input())

def func(N):
    if(N == 1):
        return 0
    # 짝수이면 2로 나누고, 홀수이면 3으로 나누기    
    if(N % 2 == 0):
        return func(N // 2) + 1
    else:
        return func(N // 3) + 1
    
print(func(N))