A, B, C = map(int, input().split())

answer = 0

for i in range(C // A + 1):
    cnt = A * i # A를 i번 사용

    num_B = (C - cnt) // B # 값을 최대로 하기 위해 B를 몇 번 사용해야 하는가

    cnt += num_B * B

    answer = max(answer, cnt)

print(answer)