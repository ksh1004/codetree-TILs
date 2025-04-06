N = int(input())
info = []
for i in range(N):
    a, b = map(int, input().split())
    info.append([a, b])

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            no_overlap = True
            arr = [0] * 101 # a, b는 0보다 크거나 같고 100보다는 작거나 같다
            # arr는 0~100 사이 선분이 포함되는 횟수
            for x in range(N):
                if(x == i or x == j or x == k):
                    continue
                
                for y in range(info[x][0], info[x][1] + 1):
                    arr[y] += 1
            
            for x in range(101):
                if(arr[x] > 1):
                    no_overlap = False
            
            if(no_overlap):
                cnt += 1

print(cnt)