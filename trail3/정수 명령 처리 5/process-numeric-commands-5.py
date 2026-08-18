n = int(input())

arr = []

for _ in range(n):
    command = input().split()

    if command[0] == "push_back":
        arr.append(int(command[1]))

    elif command[0] == "pop_back":
        arr.pop()

    elif command[0] == "size":
        print(len(arr))

    elif command[0] == "get":
        k = int(command[1])
        print(arr[k - 1])
