N = int(input())
A, B, C = 0, 0, 0
honor = 'ABC'
cnt = 0
for i in range(N):
    c, s = input().split()
    s = int(s)
    if(c == 'A'):
        A += s
    elif(c == 'B'):
        B += s
    elif(c == 'C'):
        C += s

    if(A == B and A > C): # A == B > C
        if(honor == 'AB'):
            continue
        else:
            honor = 'AB'
            cnt += 1
    elif(A == C and A > B): # A == C > B
        if(honor == 'AC'):
            continue
        else:
            honor = 'AC'
            cnt += 1
    elif(B == C and B > A): # B == C > A
        if(honor == 'BC'):
            continue
        else:
            honor = 'BC'
            cnt += 1            
    elif(A == B and A == C): # A == B == C
        if(honor == 'ABC'):
            continue
        else:
            honor = 'ABC'
            cnt += 1
    elif(A > B and A > C): # A 단독 최고값
        if(honor == 'A'):
            continue
        else:
            honor = 'A'
            cnt += 1
    elif(B > A and B > C): # B 단독 최고값
        if(honor == 'B'):
            continue
        else:
            honor = 'B'
            cnt += 1            
    elif(C > A and C > B): # C 단독 최고값
        if(honor == 'C'):
            continue
        else:
            honor = 'C'
            cnt += 1

print(cnt)