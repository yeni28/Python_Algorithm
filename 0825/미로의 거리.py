def bfs(i,j,N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i,j))  # 시작점 인큐
    visited[i][j] = 1  # 시작점 방문 표시

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while True:
        # 현재 위치가 도착점인지 판단:
        if arr[i][j] == 3:
            return visited[i][j] - 2

        for d in range(4):
            ni = di[d] + i
            nj = dj[d] + j
            # 다음 위치를 정한 다음 움직일 수 있는지 알아보기
            # 벽 / 2차원 배열 범위 밖/ 방문한 적 있다면 갈 수 없음
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                # 갈 수 있는 위치
                # 현재 위치를 스택에 저장
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                # 현재 위치를 다음 위치로 최신화
                i, j = ni, nj
                break  # 현재 갈 수 있는 방향으로 더 가지않고 다음 방향으로 가게된다.
        else:
            if q:
                i, j = q.pop()
            # 스택이 비어있으면 반복을 종료.
            else:
                break

    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    si = sj = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i
                sj = j #시작위치 정해주기

    print(f'#{tc} {bfs(si,sj,N)}')