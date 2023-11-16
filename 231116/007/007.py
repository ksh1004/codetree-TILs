# 객체
class cls:
    def __init__(self, code, location, time):
        self.code = code
        self.location = location
        self.time = time

code, location, time = input().split()
cls1 = cls(code, location, time)
print(f'secret code : {code}')
print(f'meeting point : {location}')
print(f'time : {time}')