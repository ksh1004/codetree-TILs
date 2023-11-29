# 해설 코드
n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
dx, dy = [0, 1, -1, 0], [1, 0, 0, -1] # 북, 동, 서, 남 순서(남, 북이 서로 반대고, 서, 동이 서로 반대임)
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}
direction = mapper[d]
for _ in range(t):
    nx, ny = r + dx[direction], c + dy[direction]
    if(1 <= nx and nx <= n and 1 <= ny and ny <= n):
        r, c = nx, ny
    else:
        direction = 3 - direction
# 출력
print(r, c)