s = input()
arr = []
for i in s:
    arr.append(i)
for i in range(len(arr)):
    if(i == 1 or i == len(s) - 2):
        print('a', end = '')
    else:
        print(arr[i], end = '')