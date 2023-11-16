class User:
    def __init__(self, id_val = 'codetree', level = '10'):
        self.id_val = id_val
        self.level = level
    
id_val, level = input().split()
user1 = User()
print(f'user {user1.id_val} lv {user1.level}')
user1.id_val = id_val
user1.level = level
print(f'user {user1.id_val} lv {user1.level}')