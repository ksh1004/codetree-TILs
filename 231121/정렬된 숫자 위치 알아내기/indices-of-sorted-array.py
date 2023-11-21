class Number:
    def __init__(self, number, first):
        self.number = number
        self.first = first
        self.last = -1

number = []
N = int(input())
num_list1 = list(map(int, input().split())) # 처음 입력받은 수열
num_list2 = [] # 최종 수열
for i in range(1, len(num_list1) + 1):
    number.append(Number(num_list1[i - 1], i))

# 이동한 위치를 저장하는 과정
number.sort(key = lambda x: (x.number, x.first))
for i in range(0, len(number)):
    number[i].last = i + 1 # 이동한 위치를 last에 저장

# 다시 입력으로 받은 순서대로 정렬 후 이동한 위치를 출력
number.sort(key = lambda x : x.first)
for i in number:
    print(i.last, end = ' ')