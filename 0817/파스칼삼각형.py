T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1] #점화식
    print(f'#{tc}')

    #print(arr[4][3]) => 4C3의 개수 랑 같다
    for n in range(N):
        for m in range(N):
            if arr[n][m]:
                print(arr[n][m], end=' ')
        print()