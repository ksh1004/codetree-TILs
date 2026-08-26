K, N = map(int, input().split())
arr = []

def print_permutation():
    for num in arr:
        print(num, end = ' ')
    print()

def find_permutations(cnt):
    if(cnt == N): # N개를 모두 뽑은 경우
        print_permutation()
        return
    # 1부터 k까지 각 숫자가 뽑혔을 때의 경우를 탐색
    for i in range(1, K + 1):
        arr.append(i)
        find_permutations(cnt + 1)
        arr.pop()
    
find_permutations(0)