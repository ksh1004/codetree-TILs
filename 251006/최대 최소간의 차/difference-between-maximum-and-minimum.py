def solve():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + arr[i]

    ans = float('inf')
    j = 0

    for i in range(N):
        # arr[i]를 L로 잡았을 때 [L, L+K] 안에 들어가는 구간의 오른쪽 끝 찾기
        while j < N and arr[j] <= arr[i] + K:
            j += 1

        # [i, j-1] 구간이 안에서 유지되는 부분
        # 왼쪽 비용 (arr[0..i-1]을 arr[i]로 올리기)
        left_cost = arr[i] * i - prefix[i]

        # 오른쪽 비용 (arr[j..N-1]을 arr[i]+K로 내리기)
        right_cost = (prefix[N] - prefix[j]) - (arr[i] + K) * (N - j)

        total_cost = left_cost + right_cost
        ans = min(ans, total_cost)

    print(ans)


if __name__ == "__main__":
    solve()