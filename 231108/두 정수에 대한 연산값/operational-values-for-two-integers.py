a, b = map(int, input().split())

def func(num1, num2):
    max_val = max(num1, num2)
    min_val = min(num1, num2)
    max_val += 25
    min_val *= 2
    return min_val, max_val

n1, n2 = func(a, b)
print(n1, n2)