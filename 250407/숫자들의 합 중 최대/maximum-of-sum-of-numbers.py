X, Y = map(int, input().split())

max_sum = 0
# 숫자들의 합 중 최대를 구하기
for i in range(X, Y + 1):
    val = str(i) # i 값을 문자로 변환
    i_sum = 0 # i의 숫자들의 합을 저장할 변수
    for j in range(len(val)):
        now_val = int(val[j]) 
        i_sum += now_val
    max_sum = max(max_sum, i_sum)
# 출력
print(max_sum)