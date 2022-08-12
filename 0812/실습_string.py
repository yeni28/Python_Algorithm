

def BF(p, t):
    i = 0
    j = 0
    cnt = 0

    for s in range(N):
        while j < M and i < N:
            if t[i] == p[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        if j == M:
            cnt += 1
            return cnt
        else:
            return

T = 10
for tc in range(1, T + 1):
    p = input()
    t = input()
    M = len(p)
    N = len(t)
    result = BF(p, t)

    print(f'#{tc} {result}')


