T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    #행 탐색
    cnt_row = 0
    cnt_col = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if j + 1 < N:
                if arr[i][j] == 1 and arr[i][j+1] == 0:
                    if cnt == K:
                        cnt_row += 1
                        cnt = 0
                    else:
                        cnt = 0
        if cnt == K:
            cnt_row += 1


    #열 탐색
    for j in range(N):
        cnt_2 = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt_2 += 1
            if i + 1 < N:
                if arr[i][j] == 1 and arr[i + 1][j] == 0:
                    if cnt_2 == K:
                        cnt_col += 1
                        cnt_2 = 0
                    else:
                        cnt_2 = 0
        if cnt_2 == K:
            cnt_col += 1


    print(f'#{tc} {cnt_row + cnt_col}')
