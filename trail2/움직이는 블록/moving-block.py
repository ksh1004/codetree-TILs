N = int(input())
data = []
for i in range(N):
    num = int(input())
    data.append(num)

cnt = 0
val = sum(data) // N # 모든 블럭 개수가 동일할 때의 수

for i in data:
    cnt += abs(i - val)
    '''
    만약 평균 값보다 블럭 개수가 많다면,
    평균보다 더 많은 블럭 개수만 더한다.
    더 많은 블럭 개수만 옮기면 되기 때문이다
    (적은 블럭의 경우에는 평균보다 적은 만큼 부분만 채우면 됨)
    '''
cnt = cnt // 2 # 중복 제거
print(cnt)