# 객체
class Cls:
    def __init__(self, code, location, time):
        self.code = code
        self.location = location
        self.time = time

code, location, time = input().split()
cls1 = Cls(code, location, time)
print(f'secret code : {cls1.code}')
print(f'meeting point : {cls1.location}')
print(f'time : {cls1.time}')