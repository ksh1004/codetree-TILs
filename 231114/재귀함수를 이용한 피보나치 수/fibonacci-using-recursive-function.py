N = int(input())

def func(num): # 피보나치 수열: 이전 두 항의 합이 그 다음 항이 되는 수열
    if(num == 1 or num == 2):
        return 1
    # 점화식
    return func(num - 1) + func(num - 2)

print(func(N))