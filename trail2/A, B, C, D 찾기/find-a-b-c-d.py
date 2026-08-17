def solve():
    arr = list(map(int, input().split()))
    arr.sort()
    
    A = arr[0]
    B = arr[1]
    C = arr[2]
    total = arr[14]  # A + B + C + D
    D = total - A - B - C
    
    print(A, B, C, D)

solve()