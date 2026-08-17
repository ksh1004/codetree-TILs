def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    
    O = sum(1 for x in arr if x % 2 == 1)
    E = N - O
    
    for k in range(N, 0, -1):
        OG = k // 2
        EG = (k + 1) // 2
        leftover = O - OG
        if leftover < 0:
            continue
        if leftover % 2 != 0:
            continue
        if E + leftover // 2 < EG:
            continue
        print(k)
        return

solve()