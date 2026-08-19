n = int(input())
arr = list(map(int, input().split()))

# 삽입 정렬 구현
for i in range(1, n):
    key = arr[i]  # 현재 삽입할 원소
    j = i - 1
    
    # key보다 큰 원소들을 오른쪽으로 한 칸씩 이동
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        
    # 적절한 위치에 key 삽입
    arr[j + 1] = key

# 정렬된 결과 출력
print(*arr)