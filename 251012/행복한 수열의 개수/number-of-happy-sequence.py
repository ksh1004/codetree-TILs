N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)] # 격자

total = 0 # 원하는 수열의 개수
# 행에서 원하는 수열의 개수가 나오는 값
for i in range(0, N): # i : 행의 숫자
    num, cnt = 0, 0 # 해당 행에서의 연속되는 숫자 카운트
    for j in range(0, N):
        if(j == 0): # 첫 번째인 경우
            num = grid[i][j]
            cnt = 1
            if(M == cnt): # 원하는 수열에 해당하는 경우
                total += 1 # 카운팅
                break # 현재 for문 탈출
        elif(num != grid[i][j]): # 직전 숫자와 현재 숫자가 다른 경우
            num = grid[i][j] # 현재 숫자로 최신화
            cnt = 1 # 카운트 초기화
        elif(num == grid[i][j]): # 직전 숫자와 현재 숫자가 같은 경우
            cnt += 1 # 카운트 증가
            if(M == cnt): # 카운트가 M과 동일한 경우
                total += 1 # 카운팅
                break # 현재 for문 탈출
# 열에서 원하는 수열의 개수가 나오는 값
for j in range(0, N): # i : 행의 숫자
    num, cnt = 0, 0 # 해당 행에서의 연속되는 숫자 카운트
    for i in range(0, N):
        if(i == 0): # 첫 번째인 경우
            num = grid[i][j]
            cnt = 1
            if(M == cnt): # 원하는 수열에 해당하는 경우
                total += 1 # 카운팅
                break # 현재 for문 탈출
        elif(num != grid[i][j]): # 직전 숫자와 현재 숫자가 다른 경우
            num = grid[i][j] # 현재 숫자로 최신화
            cnt = 1 # 카운트 초기화
        elif(num == grid[i][j]): # 직전 숫자와 현재 숫자가 같은 경우
            cnt += 1 # 카운트 증가
            if(M == cnt): # 카운트가 M과 동일한 경우
                total += 1 # 카운팅
                break # 현재 for문 탈출
# 출력
print(total)