N = int(input())
arr = list(map(int, input().split()))

unique_sorted = sorted(set(arr)) # set으로 중복 값 지우고 정렬

if(len(unique_sorted) < 2): # 서로 다른 값이 2개 미만이면 위치 계산 불가
    print(-1)
else:
    second = unique_sorted[1]
    positions = [i + 1 for i, v in enumerate(arr) if v == second]
    '''
    enumerate(배열): 리스트 순회 시 (인덱스, 값)을 만들어줌
    arr = [1, 5, 2, 1]
    enumerate(arr)
    → [(0, 1), (1, 5), (2, 2), (3, 1)]  
    '''
    if len(positions) != 1:
        print(-1)
    else:
        print(positions[0])