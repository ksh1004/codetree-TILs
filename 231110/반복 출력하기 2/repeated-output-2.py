N = int(input())

def func(N):
    if(N == 0):
        return
    func(N - 1)
    print('HelloWorld')
    
func(N)