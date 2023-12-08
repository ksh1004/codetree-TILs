N = int(input())
arr = []
# 격자 정보 저장
for i in range(N):
    num = list(map(int, input().split()))
    arr.append(num)
# 동전 최대 개수 계산
max_val = -1
for i in range(N): # 첫 번째의 x좌표
    for j in range(N - 2): # 첫 번째의 y좌표
        for k in range(i, N): # 두 번째의 x좌표
            for l in range(N - 2): # 두 번째의 y좌표
                if(i == k): # 두 격자가 같은 행이면
                    for x in range(j + 3, N - 2):
                        num1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                        num2 = arr[k][x] + arr[k][x + 1] + arr[k][x + 2]
                        max_val = max(max_val, num1 + num2)
                else: # 두 격자가 다른 열이면
                    num1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                    num2 = arr[k][l] + arr[k][l + 1] + arr[k][l + 2]
                    max_val = max(max_val, num1 + num2)
# 출력
print(max_val)