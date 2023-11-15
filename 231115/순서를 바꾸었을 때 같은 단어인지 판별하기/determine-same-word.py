s1 = input()
s2 = input()
s1_list = []
s2_list = []
if(len(s1) != len(s2)):
    print('No')
else:
    for i in range(len(s1)):
        s1_list.append(s1[i])
        s2_list.append(s2[i])
    s1_list.sort()
    s2_list.sort()
    check_val = 1
    for i in range(len(s1)):
        if(s1_list[i] != s2_list[i]):
            check_val = 0
    if(check_val == 1):
        print('Yes')
    else:
        print('No')