input_s = input()
purpose = input()

def func(input_s, purpose):
    idx = -1
    seq = 0
    for i in range(len(input_s)):
        if(seq == 0 and input_s[i] == purpose[seq]): # 첫 문자열이 같은 경우
            idx = i
            seq += 1 # seq 1 증가
            if(seq == len(purpose)): # 만약 seq 값과 입력 문자열이 같다면(즉, 목적 문자열이 존재하면)
                break
            if(i == len(input_s) - 1 and seq < len(purpose)): # 끝까지 비교했는데 목적 문자열이 존재하지 않으면
                idx = -1
        elif(input_s[i] == purpose[seq]): # 이후 문자열이 같은 경우
            seq += 1 # seq 1 증가
            if(seq == len(purpose)): # 만약 seq 값과 입력 문자열이 같다면(즉, 목적 문자열이 존재하면)
                break
            if(i == len(input_s) - 1 and seq < len(purpose)): # 끝까지 비교했는데 목적 문자열이 존재하지 않으면
                idx = -1
        else: # 문자열이 다른 경우
            seq = 0
            if(input_s[i] == purpose[seq]): # 첫 목적 문자가 해당 문자열과 같은 경우
                idx = i # 인덱스 재설정
                seq += 1
            if(seq == len(purpose)): # 만약 인덱스 값과 입력 문자열이 같다면(즉, 목적 문자열 길이가 1이고 존재하면)
                break
            if(i == len(input_s) - 1 and seq < len(purpose)): # 끝까지 비교했는데 목적 문자열이 존재하지 않으면
                idx = -1
    return idx

print(func(input_s, purpose))