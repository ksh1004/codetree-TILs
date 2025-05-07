n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(11):
    for j in range(11):
        for k in range(11):
            success = True # success : 직선 3개로 모든 점을 지나게 할 수 있으면 true
            # x축에 평행한 직선 3개로 모든 점을 지나게 할 수 있는 경우
            for x, y in points:
                if x == i or x == j or x == k: 
                    continue # 해당 점이 직선에 닿으면 넘어감
                success = False
            if(success == True):
                answer = 1
            # x축에 평행한 직선 2개와 y축에 평행한 직선 1개로 모든 점을 지나게 할 수 있는 경우
            success = True
            for x, y in points:
                if x == i or x == j or y == k:
                    continue # 해당 점이 직선에 닿으면 넘어감
                success = False
            if(success == True):
                answer = 1
            # x축에 평행한 직선 1개와 y축에 평행한 직선 2개로 모든 점을 지나게 할 수 있는 경우
            success = True
            for x, y in points:
                if x == i or y == j or y == k:
                    continue # 해당 점이 직선에 닿으면 넘어감
                success = False
            if(success == True):
                answer = 1
            # y축에 평행한 직선 3개로 모든 점을 지나게 할 수 있는 경우
            success = True
            for x, y in points:
                if y == i or y == j or y == k:
                    continue # 해당 점이 직선에 닿으면 넘어감
                success = False
            if(success == True):
                answer = 1

print(answer)