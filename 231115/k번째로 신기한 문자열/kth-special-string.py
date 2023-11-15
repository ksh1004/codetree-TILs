n, k, T = input().split()
n, k = int(n), int(k)
str_list = []

for i in range(n):
    s = input()
    check_val = 1
    if(len(s) <= len(T)):
        for j in range(len(T)):
            if(s[j] != T[j]):
                check_val = 0
    if(check_val == 1):
        str_list.append(s)

str_list.sort()
print(str_list[k - 1])