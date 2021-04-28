res = 0
s = input()
stack = [-1]
length = len(s)
# (()
for i in range(length):
    if s[i] == "(":
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        res = max(res, i - stack[-1])
stack = [length]
for i in range(length - 1, -1, -1):
    if s[i] == ")":
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        res = max(res, stack[-1] - i)
print(res)
