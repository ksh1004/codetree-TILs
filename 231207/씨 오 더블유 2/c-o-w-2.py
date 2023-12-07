N = int(input()) # 문자열 길이
s = input() # 문자열
cnt = 0
# 문자열 갯수 계산
for i in range(N):
    if(s[i] == 'C'):
        for j in range(i + 1, N):
            if(s[j] == 'O'):
                for k in range(j + 1, N):
                    if(s[k] == 'W'):
                        cnt += 1
# 출력
print(cnt)