def can_make(arr, D, K):
    # arr의 모든 원소를 어떤 [x, x+D] 구간 안에 넣을 수 있는지 확인
    n = len(arr)
    min_val, max_val = min(arr), max(arr)
    # 구간 시작점 x를 arr 원소 기준으로 잡아보며 검사
    # 최적화를 위해 x 후보는 arr[i] ~ arr[i]+D
    possible = False
    for a in arr:
        left, right = a, a + D
        cost = 0
        for v in arr:
            if v < left:
                cost += (left - v)
            elif v > right:
                cost += (v - right)
            if cost > K:  # 이미 초과하면 중단
                break
        if cost <= K:
            possible = True
            break
    return possible


def solve():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    lo, hi = 0, max(arr) - min(arr)
    ans = hi

    while lo <= hi:
        mid = (lo + hi) // 2
        if can_make(arr, mid, K):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(ans)


if __name__ == "__main__":
    solve()
