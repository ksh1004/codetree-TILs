a, b, c, d, e = 'apple', 'banana', 'grape', 'blueberry', 'orange'
arr = [a, b, c, d, e]
s = input()
cnt = 0

for i in arr:
    if(i[2] == s or i[3] == s):
        print(i)
        cnt += 1

print(cnt)