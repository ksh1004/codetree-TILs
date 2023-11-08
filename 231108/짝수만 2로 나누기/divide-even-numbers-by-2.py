N = int(input())

def func(N):
    num_input_list = list(map(int, input().split()))
    num_output_list = []
    for i in range(N):
        if(num_input_list[i] % 2 == 0):
            num_output_list.append(num_input_list[i] // 2)
        else:
            num_output_list.append(num_input_list[i])

    for i in num_output_list:
        print(i, end = ' ')

func(N)