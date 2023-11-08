n, m = map(int, input().split())

def swap(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return [num1, num2]
    
num_val = swap(n, m)
print(num_val[0], num_val[1])