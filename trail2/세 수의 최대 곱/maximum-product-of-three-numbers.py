N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# +, +, +
v1 = arr[-1] * arr[-2] * arr[-3]
# +, -, -
v2 = arr[-1] * arr[0] * arr[1]
if(v1 >= v2):
    print(v1)
else:
    print(v2) 