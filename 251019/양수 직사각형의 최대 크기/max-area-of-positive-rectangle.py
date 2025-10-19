n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

max_size = -1

def isTrueSquare(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if grid[i][j] <= 0:
                return False
    return True

def max_square(x, y):
    # 최대 사각형 크기
    max_square_size = -1

    for i in range(x, n):
        for j in range(y, m):
            if isTrueSquare(x, y, i, j):
                size = (i - x  + 1) * (j - y + 1)
                max_square_size = max(size, max_square_size)
    return max_square_size

for i in range(n):
    for j in range(m):
        max_size = max(max_size, max_square(i, j))

print(max_size)