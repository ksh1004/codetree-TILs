num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
m1, d1, m2, d2 = map(int, input().split())

# 두 날짜의 총 일수 구하기
total_day1, total_day2 = 0, 0
for i in range(1, m1):
    total_day1 += num_of_days[i]
total_day1 += d1
for i in range(1, m2):
    total_day2 += num_of_days[i]
total_day2 += d2

# 두 날짜 간 차이 구하기
diff = total_day2 - total_day1
#while(diff < 0): # 음수인 경우에는 양수로 전환
#    diff += 7
diff %= 7
print(day[diff])