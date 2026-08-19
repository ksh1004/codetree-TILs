import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 병합에 필요한 임시 배열
merged_arr = [0] * n

def merge(low, mid, high):
    i = low
    j = mid + 1
    k = low

    # 두 분할 영역을 비교하며 정렬된 순서로 임시 배열에 합침
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merged_arr[k] = arr[i]
            i += 1
        else:
            merged_arr[k] = arr[j]
            j += 1
        k += 1

    # 왼쪽 영역에 남아있는 원소들 복사
    while i <= mid:
        merged_arr[k] = arr[i]
        i += 1
        k += 1

    # 오른쪽 영역에 남아있는 원소들 복사
    while j <= high:
        merged_arr[k] = arr[j]
        j += 1
        k += 1

    # 임시 배열의 결과를 원본 배열에 복사
    for idx in range(low, high + 1):
        arr[idx] = merged_arr[idx]

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)        # 왼쪽 절반 분할
        merge_sort(mid + 1, high)   # 오른쪽 절반 분할
        merge(low, mid, high)       # 정렬하며 병합

# 병합 정렬 수행 (인덱스 0부터 n-1까지)
merge_sort(0, n - 1)

# 정렬된 결과 출력
print(*arr)