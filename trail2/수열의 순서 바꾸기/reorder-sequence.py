def solve():
    N = int(input())
    a = list(map(int, input().split()))
    
    L = 1  # 마지막 원소 하나는 항상 "증가하는 접미사"
    for i in range(N - 2, -1, -1):
        if a[i] < a[i + 1]:
            L += 1
        else:
            break
    
    print(N - L)

solve()