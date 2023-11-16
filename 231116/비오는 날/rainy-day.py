class Data:
    def __init__(self, day, date, weather):
        self.day = day
        self.date = date
        self.weather = weather

n = int(input())
data_list = []

for i in range(n):
    day, date, weather = input().split()
    if(weather == 'Rain'):
        data_list.append(Data(day, date, weather))

day_list = []

for i in range(len(data_list)):
    day_list.append(data_list[i].day)

day_list.sort()
day_val = day_list[0]

for i in range(len(data_list)):
    if(day_val == data_list[i].day):
        print(f'{data_list[i].day} {data_list[i].date} {data_list[i].weather}')
        break