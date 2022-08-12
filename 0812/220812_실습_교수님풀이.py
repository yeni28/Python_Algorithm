def bruteforce(p, t):
    ti = 0
    pi = 0
    tl = len(t)
    pl = len(p)

    cnt = 0 #패턴 일치 횟수

    while pi < pl and ti < tl:
        if t[ti] != p[pi]:
            ti = ti - pi
            pi = -1
        ti += 1
        pi += 1
        if pi == pl: #while문 안에서 해주면 패턴 인덱스가 패턴 길이만큼 됐다면 일치하는 패턴을 찾았다라는 의미
            cnt += 1
            # 계속 탐색을 이어나가기 위해
            pi = 0 #패턴 위치는 0으로(제일 처음으로)
            ti += 1 #텍스트 인덱스는 1 증가

        return cnt
    T = 10

    for tc in range(1, T + 1):
        p = input()
        t = input()

        result = bruteforce(p, t)

        print(f'#{tc} {result}')



