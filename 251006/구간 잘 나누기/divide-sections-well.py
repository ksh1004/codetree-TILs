MAX_A = 10000

#변수 선언 및 입력
n, m = tuple(map(int, input().split()))

a = list(map(int, input().split()))

# 구간의 합의 최댓값을 결정한다면 구간을 몇 개로 나눠야 하는지 손쉽게 찾을 수 있다.
ans = MAX_A
for i in range(1, MAX_A + 1):
    # 구간의 합의 최댓값이 i일 때

    # possible : 구간을 나눌 수 있으면 true
    # section : 나뉘어져야 하는 구간의 개수
    possible = True
    section = 1

    cnt = 0
    for j in range(n):
        # 숫자 하나가 i보다 크면 구간을 나눌 수 없다.
        if a[j] > i:
            possible = False
            break
        
        # j번째 숫자가 들어갔을 때 i보다 커지면 j번째 숫자부터 다음 구간으로 만든다.
        if cnt + a[j] > i:
            cnt = 0
            section += 1

        # 이번 구간에 j번째 숫자를 집어넣는다.
        cnt += a[j]

    if possible and section <= m:
        ans = min(ans, i)

print(ans)