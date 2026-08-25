s = input().strip()

stack = []
valid = True

for ch in s:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        if not stack:
            valid = False
            break
        stack.pop()

if stack:
    valid = False

print("Yes" if valid else "No")