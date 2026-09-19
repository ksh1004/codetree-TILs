import sys

n = int(input())
time = []
prereq_count = []
prereq = []

for _ in range(n):
    line = list(map(int, input().split()))
    time.append(line[0])
    prereq_count.append(line[1])
    prereq.append(line[2:])

# Please write your code here.
sys.setrecursionlimit(10000)

finish = [0] * (n + 1)  # finish[i] = 작업 i가 끝나는 시각 (1-indexed)
visited = [False] * (n + 1)


def get_finish_time(task):
    # 이미 계산된 경우 캐시된 값 반환 (메모이제이션)
    if visited[task]:
        return finish[task]

    visited[task] = True

    idx = task - 1  # 0-indexed 리스트 접근용
    if prereq_count[idx] == 0:
        finish[task] = time[idx]
    else:
        max_prereq_finish = 0
        for p in prereq[idx]:
            max_prereq_finish = max(max_prereq_finish, get_finish_time(p))
        finish[task] = max_prereq_finish + time[idx]

    return finish[task]


answer = 0
for task in range(1, n + 1):
    answer = max(answer, get_finish_time(task))

print(answer)