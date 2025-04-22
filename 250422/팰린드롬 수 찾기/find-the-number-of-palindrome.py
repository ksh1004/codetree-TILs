X, Y = map(int, input().split())
cnt = 0
for i in range(X, Y + 1):
    num1 = str(i)
    num2 = num1[::-1]
    if(num1 == num2):
        cnt += 1
print(cnt)