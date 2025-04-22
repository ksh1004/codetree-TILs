from typing import List

def compute_adjacent_diff_sum(numbers: List[int]) -> int:
    """리스트 내 인접한 수들의 차이의 합을 계산"""
    return sum(abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers)))

def find_min_diff_after_double_and_remove(numbers: List[int]) -> int:
    """하나를 두 배로 만들고, 또 다른 하나를 제거했을 때 인접 차이 합의 최솟값 계산"""
    n = len(numbers)
    min_total = float('inf')

    for i in range(n):
        numbers[i] *= 2  # i번째 원소를 두 배로
        for j in range(n):
            if i == j:
                continue  # 같은 원소를 두 배 후 제거하지 않음
            temp_list = [numbers[k] for k in range(n) if k != j]  # j번째 원소 제거
            diff_sum = compute_adjacent_diff_sum(temp_list)
            min_total = min(min_total, diff_sum)
        numbers[i] //= 2  # 원상 복구

    return min_total

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    result = find_min_diff_after_double_and_remove(numbers)
    print(result)

if __name__ == "__main__":
    main()
