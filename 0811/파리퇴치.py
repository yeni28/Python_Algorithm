T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    for fly in range(N):
        area = [list(map(int, input().split()))]

        for i in range(N):
            for j in range(N):
                cnt = 0
                for k in range(M):







    print(f'#{tc} {cnt}')
