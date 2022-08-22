T = int(input())
for tc in range(1,T+1):
    sticks = input()
    stack = 0
    result = 0 #쇠막대기의 조각

    for i in range(len(sticks)): #input의 괄호를 돌면서
        if sticks[i] == '(': #만약 여는 괄호라면
            stack += 1 #스택에 1 추가
        else: #닫는 괄호라면
            stack -= 1 #스택에 1 감소
            #그 이전이 만약 여는괄호라면
            if sticks[i - 1] == '(':
                result += stack #스택의 값만큼 조각을 추가
            else:
                result += 1
