N = int(input())
A, B = 0, 0 # 시작 점수 0
honor = 'AB' # A와 B 둘 다 명예의 전당에 등재
cnt = 0 # 명예의 전당이 바뀌는 횟수를 기록할 변수
for i in range(N):
    student, point = input().split()
    point = int(point)
    # 점수 입력
    if(student == 'A'):
        A += point
    else:
        B += point
    
    # 점수 변동 계산
    if(A > B): # A가 B보다 점수가 높다면
        if(honor == 'A'): # 명예의 전당은 여전히 A일 때
            continue
        else:
            honor = 'A'
            cnt += 1
    elif(A < B): # B가 A보다 점수가 높다면
        if(honor == 'B'): # 명예의 전당은 여전히 B일 때
            continue
        else:
            honor = 'B'
            cnt += 1
    else: # A == B
        if(honor == 'AB'): # 명예의 전당이 여전히 AB 공동일 때
            continue
        else:
            honor = 'AB'
            cnt += 1

print(cnt) # 출력