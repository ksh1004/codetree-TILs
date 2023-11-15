n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
check_val = 1 # 같은 원소로 이루어져 있는지 판단하는 변수
for i in range(n):
    if(A[i] != B[i]): # 값이 다르면
        check_val = 0
        break

if(check_val == 1):
    print('Yes')
else:
    print('No')