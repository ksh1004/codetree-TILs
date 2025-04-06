N, B = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(N)]
gifts.sort() # 선물 가격이 낮은 순으로 정렬

max_cnt = 0
for i in range(N):
    price = 0
    cnt = 0
    for j in range(N):
        if(i == j): # 반값 쿠폰 적용대상
            price += gifts[j][0] // 2 + gifts[j][1]
        else:
            price += gifts[j][0] + gifts[j][1]
        if(price <= B):
            cnt += 1
        else:
            break
    max_cnt = max(max_cnt, cnt)
    
print(max_cnt)