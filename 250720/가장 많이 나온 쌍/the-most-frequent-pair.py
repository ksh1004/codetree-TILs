n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

def count_num(first, second):
    cnt = 0
    # (first, second) 쌍이 (a, b) 혹은 (b, a)라면 그 개수를 카운트
    for a, b in pairs:
        if (first, second) in [(a, b), (b, a)]:
            cnt += 1
    return cnt

ans = 0
# 모든 쌍 (i, j)를 잡아보며 각 쌍이 몇 번씩 나왔는지를 확인하여 그 중 최댓값을 계산
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        ans = max(ans, count_num(i, j))
print(ans)