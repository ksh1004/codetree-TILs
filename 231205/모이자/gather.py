n = int(input())
num_list = list(map(int, input().split()))
# 완전탐색
min_val = 999999
for i in range(len(num_list)):
    idx = i
    distance = 0
    for j in range(len(num_list)):
        distance += abs(j - idx) * num_list[j]
    if(distance < min_val):
        min_val = distance
# 출력
print(min_val)