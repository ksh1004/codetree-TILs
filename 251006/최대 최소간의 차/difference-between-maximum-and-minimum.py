def bisect_left(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def bisect_right(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def solve():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    # 누적합
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + arr[i]

    ans = float('inf')

    for i in range(N):
        L = arr[i]
        R = L + K

        # 왼쪽 비용 (arr < L)
        li = bisect_left(arr, L)
        left_cost = L * li - prefix[li]

        # 오른쪽 비용 (arr > R)
        ri = bisect_right(arr, R)
        right_cost = (prefix[N] - prefix[ri]) - R * (N - ri)

        total_cost = left_cost + right_cost
        ans = min(ans, total_cost)

    print(ans)


if __name__ == "__main__":
    solve()
