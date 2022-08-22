isp = {'(':0, '+':1,'*':2} #스택안
icp = {'(':3, '+':1,'*':2} #스택밖

def infix_to_postfix(exp):
    stack = []
    result = []

    for token in exp:
        #피연산자
        if '0'<= token <='9':
            result.append(token)
        # 닫는 괄호라면,
        elif token ==')':
            while stack[-1] != '(': #여는 괄호가 나올때까지
                result.append(stack.pop()) #팝해서 값 추가후
                stack.pop() # 괄호쌍을 찾았으니 제거
        else:
            if stack:
                #스택이 있고, 우선순위가 높다면
                while icp[token] <= isp[stack[-1]]:
                    result.append(stack.pop()) # 값에 추가
                    if not stack: #스택이 비어있으면
                        break
            stack.append(token)
    while stack: #스택에 아직 뭔가 남아있다면
        result.append(stack.pop())
    return ''.join(result)

def calc(exp):
    stack = []
    for token in exp:
        #피연산자일 경우 스택에 쌓아준다.
        if '0'<= token <='9':
            stack.append(int(token))
        else:
            op2 = stack.pop() #뒤에오는 수
            op1 = stack.pop() # 앞에 오는 수
            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '/':
                stack.append(op1 // op2)
            elif token == '*':
                stack.append(op1 * op2)
    return stack.pop()

T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input()
    postfix = infix_to_postfix(infix)


    print(f'#{tc} {calc(postfix)}')
