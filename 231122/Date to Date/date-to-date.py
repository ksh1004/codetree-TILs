num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = map(int, input().split())
if(m1 == m2): # 월이 같은 경우
    print(d2 - d1)
else: # 월이 다른 경우
    total = 0
    for i in range(m1 + 1, m2): # m1, m2 월 사이의 날들을 더함
        total += num_of_days[i]
    total += (d2 + (num_of_days[m1] - d1) + 1) # m1, m2월의 날들을 더함
    print(total)