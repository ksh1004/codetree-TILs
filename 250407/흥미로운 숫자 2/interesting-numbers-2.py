X, Y = map(int, input().split())
cnt = 0

for i in range(X, Y + 1):
    val = str(i)
    first_val = val[0] # 첫 번째 자리의 문자 값
    second_val = ''
    first_cnt, second_cnt = 0, 0
    check_val = 1
    for j in range(len(val)):
        if(first_val == val[j]):
            if(first_cnt <= 1 or second_cnt <= 1):
                first_cnt += 1
            else:
                check_val = 0
                break
        else:
            if(second_val == ''):
                second_val = val[j]
                second_cnt += 1
            elif(second_val == val[j]):
                second_cnt += 1
            else:
                check_val = 0
                break
        if(j == (len(val) - 1)):
            if((second_cnt == 0)): # 오직 한 가지 숫자로만 되어 있는 경우
                check_val = 0
    
    # 확인
    if(check_val):
        cnt += 1
# 출력
print(cnt)