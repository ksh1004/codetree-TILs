n = int(input())
num_list = list(map(int, input().split()))

# 최대공약수 구하는 함수
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# 최소공배수 구하는 함수
def lcm(a, b):
    return a * b // gcd(a, b)


def func(num_list):
    if len(num_list) == 2:
        return lcm(num_list[0], num_list[1])
    else:
        return lcm(num_list[0], func(num_list[1:]))
    
print(func(num_list))