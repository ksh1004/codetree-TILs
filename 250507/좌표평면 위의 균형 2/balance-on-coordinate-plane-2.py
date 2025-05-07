n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# M : 가장 많은 수의 점이 있는 구역의 점의 갯수
min_M = float('inf') # 가능한 M의 최솟값

for i in range(-100, 101, 2):
    for j in range(-100, 101, 2):
        A1, A2, A3, A4 = 0, 0, 0, 0 # 좌표평면
        for x,y in points:
            if(x > i and y > j): # 1사분면에 있는 경우
                A1 += 1
            elif(x > i and y < j): # 4사분면에 있는 경우
                A4 += 1
            elif(x < i and y > j): # 2사분면에 있는 경우
                A2 += 1
            elif(x < i and y < j): # 3사분면에 있는 경우
                A3 += 1
        M = max(A1, A2, A3, A4)
        min_M = min(min_M, M)

print(min_M)