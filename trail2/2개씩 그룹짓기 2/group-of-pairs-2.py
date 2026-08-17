def solve():
    N = int(input())  # N (그룹의 개수)
    a = list(map(int, input().split()))  # 2N개의 정수
    a.sort()
    
    ans = min(a[i + N] - a[i] for i in range(N))
    print(ans)

solve()