A = input()
cnt = 0
for i in range(len(A)):
    if(A[i] == '('):
       if(i != len(A) - 1 and A[i + 1] == '('):
        for j in range(i + 2, len(A)):
            if(j != len(A) - 1 and A[j] == ')'):
                if(A[j + 1] == ')'):
                    cnt += 1
# 출력
print(cnt)