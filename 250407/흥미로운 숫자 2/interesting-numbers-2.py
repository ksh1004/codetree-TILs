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
            first_cnt += 1
        elif(second_val == ''):
            second_val = val[j]
            second_cnt += 1
        elif(second_val == val[j]):
            second_cnt += 1
        else:
            check_val = 0
            break
    if((check_val == 1) and (first_cnt > 1 and second_cnt == 1)
    or (first_cnt == 1 and second_cnt > 1)):
        cnt += 1
    
# 출력
print(cnt)