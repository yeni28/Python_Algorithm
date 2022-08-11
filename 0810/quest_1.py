T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # 델타 배열
    # di => i가 상하좌우로 바뀔 때 어떻게 바뀌는지
    # dj => j가 상하좌우로 바뀔 때 어떻게 바뀌는지
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    sum_all_abs = 0
    # 행 우선순회 i부터 시작
    # 안에있는 반복문은 j로
    for i in range(N):
        for j in range(N):
            sub_abs = 0 #i,j의 위치에서 상하좌우 탐색, 부분합 개념
            for d in range(4):
                # 4방향 탐색
                ni = i + di[d] #next i
                nj = j + dj[d] #next j
                #다음으로 이동할 위치가 유효한 인덱스 범위인지 검사
                if 0<= ni < N and 0 <= nj < N:
                    #ni, nj is valid
                    # sum_abs += abs(arr[i][j] - arr[ni][nj])
                    sub = arr[i][j] - arr[ni][nj] if arr[i][j] - arr[ni][nj] >0 else -1 * (arr[i][j] - arr[ni][nj])
                    sub_abs += sub
            sum_all_abs += sub_abs

    print(f'#{tc} {sum_all_abs}')