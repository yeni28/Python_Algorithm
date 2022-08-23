def Forth(exp):
    stack = []
    result = ""
    for token in exp:
        # 숫자일 때
        if '0' <= token <= '9':
            stack.append(int(token))
        elif token == '.':
            if not stack:
                return 'error'
            elif 1 < len(stack): # 계산식이 끝났는데 숫자가 더 남아있다면
                return 'error'
            result = stack.pop()
        else: # 연산자를 만나면
            if len(stack) == 1: # 계산해야하는 숫자가 하나밖에 없다면
                return 'error'
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '/':
                stack.append(num1 // num2)
            elif token == '*':
                stack.append(num1 * num2)

    return result


T = int(input())
for tc in range(1, T + 1):
    exp = input().split()

    print(f'#{tc} {Forth(exp)}')
