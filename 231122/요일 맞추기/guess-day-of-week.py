num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
m1, d1, m2, d2 = map(int, input().split())
if((m1 < m2) or (m1 == m2 and d1 < d2)): # m1월 d1일이 m2월 d2일 보다 앞의 날짜인 경우
    if(m1 == m2): # 월이 같은 경우
        total = (d1 - d2) % 7
        print(day[total])
    else: # 월이 다른 경우
        total = (num_of_days[m1] - d1)
        for i in range((m1 + 1), m2):
            total += num_of_days[i]
        total += d2
        total %= 7
        print(day[total])
else: # m1월 d1일이 m2월 d2일 보다 뒤의 날짜인 경우
    if(m1 == m2): # 월이 같은 경우
        total = (d2 - d1) % 7
        print(day[total])
    else: # 월이 다른 경우
        total = (num_of_days[m2] - d2)
        for i in range((m2 + 1), m1):
            total += num_of_days[i]
        total += d1
        total %= 7
        print(day[total])