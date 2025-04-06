N, B = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(N)]
gifts.sort() # 선물 가격이 낮은 순으로 정렬

max_cnt = 0
for i in range(N):
    price = 0
    cnt = 0
    price += gifts[i][0] // 2 + gifts[i][1] # 할인 쿠폰 사용 가격

    if(price > B): # 할인 쿠폰 적용해도 예산 초과시
        continue # 패스
    cnt += 1
    other = [] # 나머지 선물 값들을 저장할 리스트
    for j in range(N):
        if(i == j):
            continue
        other.append(gifts[j][0] + gifts[j][1])
    
    other.sort() # 선물 값들을 정렬
    for i in other:
        price += i
        if(price <= B): # 예산 초과가 아닌 경우
            cnt += 1 # 추가
        else: # 예산 초과시
            break # 종료
    max_cnt = max(max_cnt, cnt)

# 출력
print(max_cnt)