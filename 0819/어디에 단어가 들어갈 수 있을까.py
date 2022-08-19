T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 2차원 배열 입력받기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행방향으로 k 만큼 비어있는지 체크한다.
    cnt_row = 0
    for i in range(N):
        row_len = 0
        for j in range(N):
            if j + 1 < N:
                if arr[i][j] == 1:
                    row_len += 1
                    if arr[i][j+1] == 0:
                        break
        if row_len == K:
            cnt_row += 1
    print(cnt_row)

    # 열방향으로 k 만큼 비어있는지 체크한다.
    cnt_col = 0
    for j in range(N):
        col_len = 0
        for i in range(N):
            if i + 1 < N:
                if arr[i][j] == 1:
                    col_len += 1
                    if arr[i+1][j] == 0:
                        break

        if col_len == K:
            cnt_col += 1
    print(cnt_col)

    print(f'#{tc} {cnt_row + cnt_col}')

