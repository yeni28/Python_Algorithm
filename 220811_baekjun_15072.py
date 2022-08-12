
for tc in range(1, 11):
    t = int(input())
    l = list(map(int, input().split()))
    a = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    for j in range(102):
        if a[99][j] == 2:
            c = j

    d = 0
    r = 99

    while True:
        if r == 0:
            break
        if a[r][c - 1]:
            d = 2
            while True:
                r += dr[d]
                c += dc[d]
                if a[r][c - 1] == 0:
                    break

        elif a[r][c + 1]:
            d = 1
            while True:
                r += dr[d]
                c += dc[d]
                if a[r][c + 1] == 0:
                    break

        d = 0
        r += dr[d]
        c += dc[d]

        print(f'#{tc} {c-1}')