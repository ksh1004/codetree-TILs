a, b, c = map(int, input().split())
total = 0
if(a == 11): # a가 11일이면
    total += ((b - 1) - a) * 60 + (60 - 11) + (c)
    print(total)
else: # a가 11일이 아니면
    total += (24 - 11) * 60 + (60 - 11)
    total += ((a - 1) - 11) * 24 * 60
    total += (b - 1) * 60 + c
    print(total)