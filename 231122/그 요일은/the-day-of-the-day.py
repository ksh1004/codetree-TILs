num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
m1, d1, m2, d2 = map(int, input().split())
A = input()
day_val = 0
for i in range(len(day)):
    if(A == day[i]):
        day_val = i

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
diff -= day_val # A 요일 위치 맞추기(만약 A요일이 화요일이면, 시작 일을 월요일 -> 화요일로 바꾸는 과정)
cnt = diff // 7 + 1
print(cnt)