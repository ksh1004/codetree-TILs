n, m = map(int, input().split())
num_list = list(map(int, input().split()))

def func(m):
    for i in range(m):
        sum_val = 0
        a1, a2 = map(int, input().split())
        for j in range(a1 - 1, a2):
            sum_val += num_list[j]
        print(sum_val)

func(m)