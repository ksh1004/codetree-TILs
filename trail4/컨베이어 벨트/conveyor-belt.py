N, T = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(T):
    # u에서 가장 오른쪽에 있는 값을 temp에 저장
    temp = u[-1]
    
    # 위에 있는 숫자들을 완성
    for i in range(N - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[N - 1]

    # 아래에 있는 숫자들을 완성
    for i in range(N - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp
    
for elem in u:
    print(elem, end = ' ')
print()

for elem in d:
    print(elem, end = ' ')
print()