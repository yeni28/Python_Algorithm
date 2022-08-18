T = 10
for tc in range(1, T+1):
    a, sentence = input().split()
    stack = []
    for i in sentence:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    pwd = ""
    for j in stack:
        pwd += j
    print(f'#{tc} {pwd}')