s = input()
str_list = []

for i in range(len(s)):
    str_list.append(s[i])

str_list.sort()
for i in str_list:
    print(i, end = '')