N, M, K = map(int, input().split())
num_list = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
for i in range(1, M + 1):
    num = int(input())
    for j in range(1, N + 1):
        if(j == num):
            num_list[j][i] = num_list[j][i - 1] + 1    
        else:
            num_list[j][i] = num_list[j][i - 1]
# 최초의 벌금을 내는 학생 찾기         
idx = -1 # 해당 학생을 저장하는 인덱스
for i in range(M + 1):
    if(i < K):
        continue
    else:
        for j in range(1, N + 1):
            if(num_list[j][i] == K): # K 번 이상 벌칙을 받은 최초의 학생 발견시
                idx = j # 해당 학생 인덱스로 저장
                break
    if(idx != -1): # 학생을 찾은 경우
        break # for문 종료
# 출력
print(idx)