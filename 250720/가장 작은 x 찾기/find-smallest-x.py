MAX_NUM = 10000

# 변수 선언 및 입력:
n = int(input())
conditions = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# x에서 시작하는 것이 가능한지 판단
def satisfy(x):
    for a, b in conditions:
        # 계속 2배씩 해주며 a <= x <= b를 항상 만족하는지 확인
        # 아니라면, False를 반환
        x *= 2
        if x < a or x > b:
            return False
    return True

# 가능한 모든 범위에 대해 탐색
# 1 ~ MAX_NUM 사이가 아니라면 애초에 처음부터 불가능
for x in range(1, MAX_NUM + 1):
    # 만족하는 x가 있다면 해당 x가 최소이므로 출력
    if satisfy(x):
        print(x)
        break