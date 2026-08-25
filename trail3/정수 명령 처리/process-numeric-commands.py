N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
stack = []
result = []

for i in range(N):
    cmd = command[i]
    if cmd == "push":
        stack.append(value[i])
    elif cmd == "pop":
        if stack:
            result.append(stack.pop())
        else:
            result.append(-1)
    elif cmd == "size":
        result.append(len(stack))
    elif cmd == "empty":
        result.append(1 if not stack else 0)
    elif cmd == "top":
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

print('\n'.join(map(str, result)))