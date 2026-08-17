def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0
    last_covered = -1  # 마지막으로 커버된 위치 (초기값: 아무것도 커버 안 됨)

    for i in range(n):
        pos = i + 1  # 1-indexed 위치
        if arr[i] == 1 and pos > last_covered:
            # 이 사람을 아직 못 덮었으므로 와이파이 설치
            count += 1
            last_covered = pos + 2 * m  # (pos + m)에 설치 시 커버 범위의 끝

    print(count)

solve()