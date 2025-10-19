X = int(input())

speed = 1 # 속도
time = 0 # 시간
distance = 0 # 거리

while(distance < X):
    # 다음 속도로 이동했을 때 삼각수 거리
    # 삼각수 : 1 + 2 + ... + k = k(k+1) / 2
    next_speed_distance = (speed + 1) * (speed + 2) // 2
    current_speed_distance = speed * (speed + 1) // 2

    # 현재 속도로 이동
    distance += speed
    time += 1

    # 속도 조정 로직
    if(distance + next_speed_distance <= X): # 한 단계 더 가속해도 아직 목표를 넘지 않는다
        speed += 1
    elif(distance + current_speed_distance <= X): # 가속하면 넘지만, 지금 속도로 유지하면 딱 맞다
        speed = speed
    else: # 이제 감속해야 한다
        speed -= 1

# 최단 시간 출력
print(time)