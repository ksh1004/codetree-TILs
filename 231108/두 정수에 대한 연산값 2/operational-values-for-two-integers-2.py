a, b = map(int, input().split())

def func(num1, num2):
    if(num1 == max(num1, num2)):
        num1 *= 2
        num2 += 10
    else:
        num1 += 10
        num2 *= 2
    
    return num1, num2

num1, num2 = func(a, b)
print(num1, num2)