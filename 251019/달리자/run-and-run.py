# 변수 선언 및 입력
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0

# 입력으로 주어진 사람 수를 보고
# 최소 어느 만큼의 거리를 달려야 하는지 확인합니다.
for i in range(n):
    if a[i] > b[i]:
        # 최소 a[i] - b[i]명의 사람들은 오른쪽으로 달려야 합니다.
        num = a[i] - b[i]
        a[i] -= num
        a[i + 1] += num
        ans += num

print(ans)