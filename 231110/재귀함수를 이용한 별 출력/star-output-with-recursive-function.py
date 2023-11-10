N = int(input())

def func(num1, num2):
    if(num1 > num2):
        return
    print(num1 * '*')
    func(num1 + 1, num2)

func(1, N)