T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    terminal = [0] * 1001
    max_route = 0
    for i in range(N):
        t, A, B = map(int, input().split())
        if t == 1 :
            for nomal in range(A, B+1):
                terminal[nomal] += 1
        elif t == 2:
            if A % 2 == 0:
                for speed in range(A, B+1):
                    if speed % 2 == 0:
                        terminal[speed] += 1
            elif A % 2 == 1:
                for speed in range(A, B+1):
                    if speed % 2 == 1:
                        terminal[speed] += 1
        elif t == 3:
            if A % 2 == 0:
                for g in range(A, B + 1):
                    if g % 4 == 0:
                        terminal[g] += 1
            elif A % 2 == 1:
                for g in range(A, B + 1):
                    if g % 3 == 0 and g % 10 != 0:
                        terminal[g] += 1
        for tm in range(len(terminal)):
            if max_route <= terminal[tm]:
                max_route = terminal[tm]
    print(f'#{tc} {max_route}')