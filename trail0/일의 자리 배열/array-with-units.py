A, B = map(int, input().split())

arr = [A, B]
for i in range(8):
    num = (arr[i] + arr[i + 1]) % 10
    arr.append(num)

for i in arr:
    print(i, end = ' ')