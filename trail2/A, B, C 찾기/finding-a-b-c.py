def solve():
    arr = list(map(int, input().split()))
    arr.sort()
    
    A = arr[0]
    B = arr[1]
    total = arr[6]  # A + B + C
    C = total - A - B
    
    print(A, B, C)

solve()