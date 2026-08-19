import sys
input = sys.stdin.readline

# 파이썬의 재귀 깊이 제한 해제
sys.setrecursionlimit(100000)

n = int(input())
arr = list(map(int, input().split()))

def partition(low, high):
    pivot = arr[high]  # 맨 오른쪽 원소를 피벗으로 선택 (Lomuto 분할 방식)
    i = low - 1        # 피벗보다 작은 원소들이 들어갈 위치의 인덱스

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 피벗을 올바른 위치(i + 1)로 이동
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(low, high):
    if low < high:
        # 피벗을 기준으로 배열을 두 부분으로 분할
        pos = partition(low, high)

        # 피벗을 제외한 왼쪽 및 오른쪽 부분 배열을 재귀적으로 정렬
        quick_sort(low, pos - 1)
        quick_sort(pos + 1, high)

# 퀵 정렬 수행 (인덱스 0부터 n-1까지)
quick_sort(0, n - 1)

# 정렬된 결과 출력
print(*arr)