N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0 # 만족하는 수열의 갯수

B.sort() # B의 수열을 크기 순으로 정렬
for i in range(N - M + 1): # 0 부터 N - M 까지
    temp = [] # 현재 A의 연속 부분 수열
    for j in range(i, i + M):
        temp.append(A[j])
    temp.sort() # temp의 수열을 크기 순으로 정렬
    if(temp == B): # temp와 B가 같으면
        cnt += 1 # 갯수 증가
# 출력
print(cnt)