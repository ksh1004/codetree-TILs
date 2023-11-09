n, m = map(int, input().split())
A = list(map(int, input().split()))

def func(num, num_list):
    sum_val = 0 # m번째 원소를 계속 더해 출력하는 값
    idx_list = [] # m번째 원소를 저장하는 리스트
    idx_list.append(num)
    while(num != 1): # num이 1이 될 때까지 값을 구하기
        if(num % 2 == 0): # 짝수면
            num //= 2 # 나누기 2
        else: # 홀수면
            num -= 1 # 빼기 1
        idx_list.append(num)
    for i in range(len(idx_list)):
        sum_val += num_list[idx_list[i] - 1] # sum_val에 더하기
    return sum_val

print(func(m, A))