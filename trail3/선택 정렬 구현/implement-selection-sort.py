n = int(input())
arr = list(map(int, input().split()))

# 선택 정렬 구현
for i in range(n - 1):
    # i번째 위치에 들어갈 최솟값의 인덱스를 찾기
    min_idx = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
            
    # 최솟값과 현재 위치(i)의 원소를 교환(Swap)
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 정렬된 결과 출력 (공백으로 구분)
print(*arr)