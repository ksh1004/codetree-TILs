A = input()

def func(s):
    s1 = s[0]
    if(len(s) == 1):
        return 0
    else:
        for i in range(1, len(s)):
            if(s1 != s[i]):
                return 1
            else:
                if(i == len(s) - 1):
                    return 0

if(func(A) == 1):
    print('Yes')
else:
    print('No')