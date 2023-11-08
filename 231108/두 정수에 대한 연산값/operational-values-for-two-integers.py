a, b = map(int, input().split())

def func(num1, num2):
    max_val = max(num1, num2)
    min_val = min(num1, num2)
    if(num1 == max_val):
        num1 += 25
        num2 *= 2
        return num1, num2
    else:
        num1 *= 2
        num2 += 25
        return num1, num2

n1, n2 = func(a, b)
print(n1, n2)