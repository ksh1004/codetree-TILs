n = int(input())
arr = list(map(int, input().split()))

def radix_sort(arr):
    # 배열에서 가장 큰 수를 찾아 최대 자릿수 구하기
    max_val = max(arr)
    
    # 1의 자리부터 시작하여 자릿수를 올리며 반복 (1, 10, 100, ...)
    p = 1
    while max_val // p > 0:
        # 0부터 9까지의 자릿수를 저장할 10개의 버킷(Bucket) 생성
        buckets = [[] for _ in range(10)]
        
        # 각 숫자의 현재 자릿수에 해당하는 버킷에 담기
        for num in arr:
            digit = (num // p) % 10
            buckets[digit].append(num)
        
        # 버킷에 담긴 순서대로 다시 하나의 배열로 합치기
        arr = []
        for bucket in buckets:
            for num in bucket:
                arr.append(num)
                
        # 다음 자릿수(10의 자리, 100의 자리...)로 이동
        p *= 10
        
    return arr

# 기수 정렬 수행 및 결과 출력
sorted_arr = radix_sort(arr)
print(*sorted_arr)