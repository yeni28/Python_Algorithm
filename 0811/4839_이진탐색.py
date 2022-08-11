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