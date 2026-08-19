n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    for j in range(0, n - 1 - i):
        # 인접한 두 원소를 비교하여 앞의 수가 더 크면 위치 교환(Swap)
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 정렬된 결과 출력
print(*(arr))