T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0

    # 가로
    for i in range(N):
        cnt_row = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt_row += 1
            if cnt_row > max_len:
                max_len = cnt_row
            if j + 1 < M:
                if arr[i][j] == 1 and arr[i][j + 1] == 0:
                    cnt_row = 0

    # 세로
    for j in range(M):
        cnt_col = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt_col += 1
            if cnt_col > max_len:
                max_len = cnt_col
            if i + 1 < N:
                if arr[i][j] == 1 and arr[i + 1][j] == 0:
                    cnt_col = 0

    print(f'#{tc} {max_len}')
