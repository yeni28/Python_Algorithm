T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_V = 0
    for i in range(N):
        for j in range(N):
            cnt = 0 #초기화 위치 주의
            # 행 M칸, 열 M칸으로 탐색하기
            for m in range(M): # M x M 행 탐색
                for k in range(M):# M x M 열 탐색
                    if 0 <= i + m < N and 0 <= j + k < N: #범위 안벗어나게! 주의
                        cnt += arr[i + m][j + k]
            if max_V < cnt: #max_V 위치 주의
                max_V = cnt

    print(f'#{tc} {max_V}')