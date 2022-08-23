T = int(input())
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for tc in range(1,T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    stack = []

    for i in range(N):
        for j in range(N):


            while True:
                # 현재 위치를 방문했다고 체크
                # 현재 위치 i, j에서 갈 수 있는 곳 탐색
                # 2차원 배열에서는 상하좌우로 움직일 수 있다.

                for d in range(4):
                    ni = di[d] + i
                    nj = dj[d] + j
                    # 다음 위치를 정한 다음 움직일 수 있는지 알아보기
                    # 벽 / 2차원 배열 범위 밖/ 방문한 적 있다면 갈 수 없음
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                        # 갈 수 있는 위치
                        # 현재 위치를 스택에 저장
                        stack.append([i, j])
                        # 현재 위치를 다음 위치로 최신화
                    else:
                # 갈 수 있는 칸이 없으면?
                # pop을 해서 뒤로 다시 돌아간다.
                # 스택이 비어있으면 반복을 종료.




