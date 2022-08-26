T = int(input())

for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = list(map(int, input().split()))
        for i in range(N):
            for j in range(M):
                arr[i][j] = arr[x][y]

    print(arr)