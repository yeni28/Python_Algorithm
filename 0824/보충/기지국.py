def check(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for k in range(4):
        for s in range(1,4):
            if ord(str(arr[x][y])) - ord('A') == 0:
                nx = x + dx[s] * 1
                ny = y + dy[s] * 1
            elif ord(str(arr[x][y])) - ord('B') == 0:
                nx = x + dx[s] * 2
                ny = y + dy[s] * 2
            elif ord(str(arr[x][y])) - ord('C') == 0:
                nx = x + dx[s] * 3
                ny = y + dy[s] * 3
        # 가장먼저 해야할 것은 행렬의 범위를 벗어나는지 체크하는 것이다.
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 'H':
                    arr[nx][ny] = 'X'
    cnt = 0
    for n in range(N):
        for m in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [list(input()) for _ in range(N)]



    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
                result = check(i, j)

    print(f'#{tc} {result}')


