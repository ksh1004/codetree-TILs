N, M, Q = map(int, input().split()) # N * M 행렬 크기, 바람의 수 Q
arr = [list(map(int, input().split())) for _ in range(N)] # 건물 상태
wind = [tuple(input().split()) for _ in range(Q)] # 바람에 대한 정보

def left_wind(num): # 바람이 왼쪽에서 부는 경우
    temp = arr[num][-1] # 마지막 값을 저장
    for i in range(M - 1, 0, -1): # 바람에 맞게 옮기기
        arr[num][i] = arr[num][i - 1]
    arr[num][0] = temp # 맨 왼쪽 값까지 설정

def right_wind(num): # 바람이 오른쪽에서 부는 경우
    temp = arr[num][0] # 첫 번째 값을 저장
    for i in range(1, M): # 바람에 맞게 옮기기
        arr[num][i - 1] = arr[num][i]
    arr[num][-1] = temp # 맨 오른쪽 값까지 설정

def isSameValueExist(n1, n2): # 각 행의 열에서 같은 값이 있는지 확인
    arr1 = arr[n1]
    arr2 = arr[n2]
    for i in range(M):
        if arr1[i] == arr2[i]: # 두 행의 같은 열에서 같은 값이 있으면
            return 1 # 1 반환
    return 0 # 같은 값이 없으면 0 반환

for i in range(Q): # 바람 수만큼 진행
    r, d = wind[i]
    r = int(r) - 1 # 해당하는 행에 맞게 숫자로 변환
    # 바람 실행
    if d == 'L':
        left_wind(r)
    elif d == 'R':
        right_wind(r)
    d_up, d_down = d, d # 위층, 아래층으로 전파될 때 바람 방향 변수

    # 바람 전파 실행(위 층 방향으로)
    for j in range(r, 0, -1):
        check = isSameValueExist(j, j - 1)
        if check == 0: # 같은 값이 없으면
            break # 전파 중단
        else:
            # 바람 방향을 반대로 변환 후 바람 실행
            if d_up == 'L':
                d_up = 'R'
                right_wind(j - 1)
            elif d_up == 'R':
                d_up = 'L'
                left_wind(j - 1)
    # 바람 전파 실행(아래 층 방향으로)

    for j in range(r, N - 1):
        check = isSameValueExist(j, j + 1)
        if check == 0: # 같은 값이 없으면
            break # 전파 중단
        else:
            # 바람 방향을 반대로 변환 후 바람 실행
            if d_down == 'L':
                d_down = 'R'
                right_wind(j + 1)
            elif d_down == 'R':
                d_down = 'L'
                left_wind(j + 1)

# 출력
for i in range(N):
    for j in range(M):
        print(arr[i][j], end = ' ')
    print()