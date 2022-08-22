# stack을 쓸 때 주의할 점 : overflow가 나오지 않게끔 크게 만들어야함
# append를 쓰면 overflow가 날 일이 없다.
# pop할 때 항상 주의해야한다. -> isEmpty인지 항상 체크해야한다.

# 후위표기법으로 바꿔줄 곳을 빈리스트로하여 append해주라는말
# stack에는 연산자들만 들어간다.
# 계속해줘야하니까 while로 해줘야함


#(1)피연산자- 출력 (2) 연산자(사칙, '(') (3) ')' - pop

infix = input()
n = len(infix)

stack = [0] * n
top = -1

result = ""

icp = {')': -, '*' : 2, '+': 1,'(':3}
isp = {')': -, '*' : 2, '+': 1,'(':0}


for i in range(n):
    # 피연산자인 경우
    if '0' <= infix[i] <= '9':
        result += infix[i]
    # 닫는 괄호일 경우
    elif infix[i] == ')':
        while infix[i] == '(':
            result += stack[top]
            top -= 1
    elif top > -1 and icp[stack[top]] >= icp[infix[i]]:
        result += stack[top]        # pop시켜주고 문자열에 출력
        top -= 1
        stack[top] = infix[i]



