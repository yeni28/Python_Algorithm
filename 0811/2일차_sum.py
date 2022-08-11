T = 10

for tc in range(1, T+1):
    no = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    for i in range(N):
        total = 0
        for j in range(N):
            total += arr[i][j]
        if max_value < total:
            max_value = total

    for i in range(N):
        total = 0
        for j in range(N):
            total += arr[j][i]
        if max_value < total:
            max_value = total

    total = 0
    for i in range(N):
        total += arr[i][i]

        if max_value < total:
            max_value = total

    total = 0
    for i in range(N):
        total += arr[100-i][100-i]

        if max_value < total:
            max_value = total

        print(f'#{tc} {max_value}')