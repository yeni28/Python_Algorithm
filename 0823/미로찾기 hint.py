def dfs(i,j,N):
    # visited = [[0] * N for _ in range(N)]

    stack = []
    di = [-1,-1,0,0]
    dj = [0,0,-1,1]

    while True:
        # 현재 위치가 도착점인지 판단:
        if arr[i][j] == 3:
            return 1
        #현재 위치를 방문했다고 체크 visited[i][j] = 1

        #방문 배열을 만들지 않고, 내가 지났던 곳을 벽으로 만들기
        arr[i][j] = 1


        # 현재 위치 i, j에서 갈 수 있는 곳 탐색
        # 2차원 배열에서는 상하좌우로 움직일 수 있다.

        for d in range(4):
            ni = di[d] + i
            nj = dj[d] + j
            # 다음 위치를 정한 다음 움직일 수 있는지 알아보기
            # 벽 / 2차원 배열 범위 밖/ 방문한 적 있다면 갈 수 없음
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1:
                # 갈 수 있는 위치
                # 현재 위치를 스택에 저장
                stack.append([i, j])
                # 현재 위치를 다음 위치로 최신화
                i, j = ni, nj
                break #현재 갈 수 있는 방향으로 더 가지않고 다음 방향으로 가게된다.
        else :
            #갈 수 있는 칸이 없으면?
            # pop을 해서 뒤로 다시 돌아간다. (pop이전 스택 비었나 확인)
            if stack:
                i, j = stack.pop()
            # 스택이 비어있으면 반복을 종료.
            else:
                break
    # 반복문이 중간에 return문을 만나 종료하지 못하고 여기까지 와버린 경우
    # 길이 없다는 이야기가 된다.
    return 0

    T = int(input())

    for tc in range(1, T + 1):
        n = int(input())
        arr = [list(map(int, input())) for _ in range(n)] #미로

        si = sj = 0  #시작 행, 열 = 0

        for i in range(n):
            for j in range(n):
                if arr[i][j] == 2:
                    si = i
                    sj = j # 시작 위치 정해주기

    print(f'#{tc} {dfs(i,j,n)}')