def solve():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    prefix = [0] * (N + 1)  # 누적합
    for i in range(N):
        prefix[i+1] = prefix[i] + arr[i]

    # 특정 구간 [L, L+D] 안에 모두 넣을 때 비용 계산
    def cost(L, D):
        R = L + D
        # 왼쪽: arr < L
        # 오른쪽: arr > R
        import bisect
        li = bisect.bisect_left(arr, L)   # arr[0..li-1] < L
        ri = bisect.bisect_right(arr, R)  # arr[ri..N-1] > R

        left_cost = L*li - prefix[li]
        right_cost = (prefix[N] - prefix[ri]) - R*(N-ri)
        return left_cost + right_cost

    # 이분 탐색
    lo, hi = 0, arr[-1] - arr[0]
    ans = hi

    while lo <= hi:
        mid = (lo + hi) // 2
        ok = False
        # arr 원소들을 시작점 후보로 잡기
        for a in arr:
            if cost(a, mid) <= K:
                ok = True
                break
        if ok:
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)


if __name__ == "__main__":
    solve()