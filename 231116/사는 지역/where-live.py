class Info:
    def __init__(self, name, code, loc):
        self.name = name
        self.code = code
        self.loc = loc

n = int(input())
class_list = []
for i in range(n):
    name, code, loc = input().split()
    class_list.append(Info(name, code, loc))

name_list = []
for i in range(n):
    name_list.append(class_list[i].name)
name_list.sort()
last_name = name_list[n - 1]
for i in range(n):
    if(class_list[i].name == last_name):
        print(f'name {class_list[i].name}')
        print(f'addr {class_list[i].code}')
        print(f'city {class_list[i].loc}')
        break