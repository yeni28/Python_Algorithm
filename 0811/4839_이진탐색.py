T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    start = 1
    end = P
    cnta = 0
    cntb = 0

    while start <= end:
        cnta += 1
        c = (int(start + end) // 2)
        if c == Pa:
            break
        elif c > Pa:
            end = c # 보기를 보면 200+1이아닌 미드값과 같은 것 확인
        elif c < Pa:
            start = c

    #while문에서 s와e가 달라져있으므로 다시 초기화를 해줘야한다.

    start = 1
    end = P
    while start <= end:
        cntb += 1 # c값이 계속 변하니까 계산마다가 아닌, c값이 변할 때마다 카운트 해줌
        c = (int(start + end) // 2)
        if c == Pb:
            break
        elif c > Pb:
            end = c
        elif c < Pb:
            start = c

    if cnta == cntb:
        result = 0
    elif cnta > cntb:
        result = 'B'
    elif cnta < cntb:
        result = 'A'

    print(f'#{tc} {result}')


    #other sol

    winner = "" #승리자
    a_start, a_end = 1, p #a의 이진탐색 범위
    b_start, b_end = 1, p #b의 이진탐색 범위

    while True:
        a_find = False #a가 페이지를 찾았는지
        b_find = False #b가 페이지를 찾았는지

        mid = (a_start + a_end) // 2

        if mid == a:
            a_find =True
        elif mid > a:
            a_end = mid
        else:
            a_start = mid
        #b의 페이지를 찾기 시작
        mid = (b_start + b_end) // 2

        if mid == b:
            b_find = True
        elif mid > b:
            b_end = mid
        else:
            b_start = mid

        if a_find and b_find: #순서를 바꾸면동시에 찾았을 떄도 A가 나오니까 맨 위로
            answer = 0
            break
        if a_find:
            answer = 'A'
            break
        if b_find:
            answer = 'B'
            break