N, M, K = map(int, input().split())
num_list = [0 for _ in range(N + 1)]
for i in range(M):
    num = int(input())
    num_list[num] += 1
idx = -1
for i in range(len(num_list)):
    if(K < i): # K 값 이전에는 최초의 값이 나올 수 없으므로 pass
        continue
    else: # K번째부터는 K값이 나올 수 있음
        for j in range(1, len(num_list)):
            if(num_list[j] >= K): # K번 이상이면 
                idx = j # 해당 학생의 번호 저장
                break
    if(idx != -1): # 최초 학생 번호가 나오면
        break # 탐색 중지
# 출력
print(idx)