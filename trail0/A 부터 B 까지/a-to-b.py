A, B = map(int, input().split())

i = A
while(i <= B):
    print(i, end = ' ')
    if(i % 2 == 0):
        i = i + 3
    else:
        i = i * 2