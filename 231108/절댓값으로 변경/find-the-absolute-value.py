N = int(input())
num_list = list(map(int, input().split()))

def abs_func(num_list):
    for i in num_list:
        print(abs(i), end = ' ')
    print()

abs_func(num_list)