N = int(input())

def func1(num):
    if(num == 0):
        return
    func1(num - 1)
    print(num, end = ' ')

def func2(num1, num2):
    if(num1 > num2):
        return
    func2(num1 + 1, num2)
    print(num1, end = ' ')

func1(N)
print()
func2(1, N)