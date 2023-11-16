class Bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time

code, color, time = input().split()
bomb1 = Bomb(code, color, time)
print(f'code : {bomb1.code}')
print(f'color : {bomb1.color}')
print(f'second : {bomb1.time}')