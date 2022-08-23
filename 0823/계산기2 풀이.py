T = 10

icp = {'+':1, '*': 2}

for tc in range(1, T + 1):
    n = int(input()) # 식의 길이

    exp = input() # 중위표현식 입력받기
    postfix = "" # 후위표현식으로 바꾼 결과

    stack = []

    for i in range(n):
        # 글자를 하나씩 떼서 보는데, 연산자 or 피연산자
        if '0' <= exp[i] <= '9': # 아스키코드 덕분에 알아서 비교
            postfix += exp[i]
        else:
            # 연산자라면, 스택의 top을 확인하여
            # 자신보다 같거나 높은 우선순위를 가진 연산자가 있으면 꺼낸다.
            if stack and icp[stack[-1]] >= icp[exp[i]]:
                postfix += stack.pop()
            stack.append(exp[i])

    # 스택에 남아있는 연산자는 뒤에 붙이기
    while stack:
        postfix += stack.pop()
    # 후위표기식 계산
    result = 0
    stack = []
    k = len(postfix)
    for i in range(k):
        # 피연산자가 나오면 그냥 넘어가고
        # 스택에다가 담는다.
        if '0' <= postfix[i] <= '9':
            stack.append(postfix[i])
        else:
            # 연산자가 나오면 계산(앞에 두 피연산자를 선택)
            # 스택에서 두개의 피연산자를 꺼낸다.
            right = int(stack.pop())
            left = int(stack.pop())

            if postfix[i] == '+':
                result = right + left
            else:
                result = right * left

            stack.append(result) # 계산하고 그 결과를 스택에 다시 넣어주기

    print(f'#{tc} {result}')
    