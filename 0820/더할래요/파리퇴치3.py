T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    #M의 세기로 스프레이를 분사, +로 분사하는 경우와 X 분사경우 비교


    max_dead_fly = 0
    more_dead = 0
    # 이동을 위한 델타 좌/우/상/하 /좌상/좌하/우하/우상
    di = [0, 0, -1, 1, -1, 1, 1, -1]
    dj = [-1, 1, 0, 0, -1, -1, 1, 1]

    for i in range(N):
        for j in range(N):
            plus_cnt = arr[i][j]
            cross_cnt = arr[i][j]
            for distance in range(1, M):
                # +로 탐색
                for move in range(4):
                    if 0 <= i + di[move] * distance < N and 0 <= j + dj[move] * distance < N:
                        plus_cnt += arr[i + di[move] * distance][j + dj[move] * distance]
                for move in range(4, 8):
                    if 0 <= i + di[move] * distance < N and 0 <= j + dj[move] * distance < N:
                        cross_cnt += arr[i + di[move] * distance][j + dj[move] * distance]

            # 탐색이 다 끝난 직후에 비교해주기!
            if cross_cnt >= plus_cnt: #카운트 해주는 것과 들여쓰기 일치시켜주는 것 잊지 말기!
                more_dead = cross_cnt
            elif cross_cnt < plus_cnt:
                more_dead = plus_cnt

            if max_dead_fly < more_dead:
                max_dead_fly = more_dead

    print(f'#{tc} {max_dead_fly}')



    # distance와 M을 착각한 것. for문 돌릴 때 변수명 잘 적기
    # range 범위를 착각한 것. 인덱스 범위 잘 체크하기
    # 들여쓰기를 착각한 것. 잘 맞춰쓰기....



