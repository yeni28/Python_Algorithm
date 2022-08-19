T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    max_len = 0

    for i in range(N):
        cnt_row: 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt_row += 1
            else:
                0
            if cnt_row > max_len:
                max_len = cnt_row
