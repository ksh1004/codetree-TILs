A = input()

def func(s):
    check_num = 0
    for i in range(len(s)):
        if(s[i] != s[len(s) - 1 - i]):
            break
        else:
            if(i == len(s) - 1):
                check_num = 1
    return check_num

if(func(A) == 1):
    print('Yes')
else:
    print('No')