n = int(input())
num_list = []
# 숫자 입력받기
for i in range(n):
    num = int(input())
    num_list.append(num)
# 계산
max_val = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 3개의 숫자를 일단 문자형으로 변환
            num1 = str(num_list[i])
            num2 = str(num_list[j])
            num3 = str(num_list[k])
            num_len = max(len(num1), len(num2), len(num3)) # 숫자가 가장 긴 값의 길이
            check_val = 0 # carry 여부를 확인
            for l in range(-1, - num_len - 1, -1):
                carry1, carry2, carry3 = 0, 0, 0
                # 숫자 자릿수와 비교하여, 숫자가 존재하면 해당 값으로 업데이트
                if(len(num1) >= abs(l)):
                    carry1 = int(num1[l])
                if(len(num2) >= abs(l)):
                    carry2 = int(num2[l])
                if(len(num3) >= abs(l)):
                    carry3 = int(num3[l])
                # carry 여부 확인
                if(carry1 + carry2 + carry3 >= 10): # carry 발생 시
                    check_val = 1 # check_val 업데이트
                    break # for문 종료
            if(check_val == 0): # carry가 아니면
                sum_val = int(num1) + int(num2) + int(num3)
                if(max_val < sum_val): # 최댓값 여부 확인
                    max_val = sum_val
# 출력
print(max_val)