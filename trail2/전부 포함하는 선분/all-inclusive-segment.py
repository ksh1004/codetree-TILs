import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    
    L = [0] * n
    R = [0] * n
    for i in range(n):
        L[i] = int(input_data[idx]); idx += 1
        R[i] = int(input_data[idx]); idx += 1
    
    INF = float('inf')
    
    prefMinL = [0] * n
    prefMaxR = [0] * n
    sufMinL = [0] * n
    sufMaxR = [0] * n
    
    prefMinL[0] = L[0]
    prefMaxR[0] = R[0]
    for i in range(1, n):
        prefMinL[i] = min(prefMinL[i - 1], L[i])
        prefMaxR[i] = max(prefMaxR[i - 1], R[i])
    
    sufMinL[n - 1] = L[n - 1]
    sufMaxR[n - 1] = R[n - 1]
    for i in range(n - 2, -1, -1):
        sufMinL[i] = min(sufMinL[i + 1], L[i])
        sufMaxR[i] = max(sufMaxR[i + 1], R[i])
    
    ans = INF
    for i in range(n):
        left_part_min = prefMinL[i - 1] if i - 1 >= 0 else INF
        right_part_min = sufMinL[i + 1] if i + 1 <= n - 1 else INF
        min_l = min(left_part_min, right_part_min)
        
        left_part_max = prefMaxR[i - 1] if i - 1 >= 0 else -INF
        right_part_max = sufMaxR[i + 1] if i + 1 <= n - 1 else -INF
        max_r = max(left_part_max, right_part_max)
        
        length = max_r - min_l
        ans = min(ans, length)
    
    print(ans)

solve()