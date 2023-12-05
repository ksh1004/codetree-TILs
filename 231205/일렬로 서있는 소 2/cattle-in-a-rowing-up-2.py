N = int(input())
num_list = list(map(int, input().split()))
cnt = 0 

for i in range(len(num_list)):
    for j in range(i + 1, len(num_list)):
        for k in range(j + 1, len(num_list)):
            if(num_list[i] <= num_list[j] <= num_list[k]):
                cnt += 1
# 출력
print(cnt)