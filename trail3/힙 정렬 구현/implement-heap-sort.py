import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def heapify(arr, n, i):
    largest = i          # 루트 노드
    left = 2 * i + 1     # 왼쪽 자식 노드
    right = 2 * i + 2    # 오른쪽 자식 노드

    # 왼쪽 자식이 존재하고 루트보다 크다면
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 존재하고 현재까지의 최대값보다 크다면
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 가장 큰 값이 루트가 아니라면 교환 후 재귀 호출
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 1. 최대 힙(Max Heap) 구성
    # 부모 노드를 가지는 마지막 노드부터 루트(0)까지 역순으로 heapify 수행
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. 힙에서 하나씩 원소를 꺼내어 배열 뒤쪽부터 정렬
    for i in range(n - 1, 0, -1):
        # 현재 루트(최대값)를 배열의 맨 뒤와 교환
        arr[0], arr[i] = arr[i], arr[0]
        # 줄어든 힙에 대해 루트 노드 기준 heapify 수행
        heapify(arr, i, 0)

heap_sort(arr)
print(*arr)