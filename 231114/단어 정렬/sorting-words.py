n = int(input())
str_list = []
for i in range(n):
    s = input()
    str_list.append(s)

str_list.sort()
for i in str_list:
    print(i)