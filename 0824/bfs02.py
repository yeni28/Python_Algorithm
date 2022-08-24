di = [-1, 1, 0, 0]        #상/하/좌/우
dj = [0, 0, -1, 1]

# 2차원 배열을 너비 우선 탐색으로 탐색하는 bfs 함수를 작성
def bfs(si, sj, n): #n은 2차원 배열의 크기, n * n
    visited = [[0] * n for _ in range(n)]
    queue = []
    queue.append((si,sj))
    visited[si][sj] = 1

    while queue:
        #현재 방문 위치 꺼내기
        i, j = queue.pop(0)
        print('=========')
        for k in range(n):
            print(visited[k])
        print('=========')




        # 현재 위치에서 갈 수 있는 곳 검사(델타를 이용한 4방향 탐색)
        for d in range(4):
            # 다음 위치 알아내기 (행, 열)
            ni = i + di[d] # 다음 행
            nj = j + dj[d] # 다음 열
            # 다음 위치가 탐색이 가능한 위치인지 검사(배열 범위를 벗어나지는 않았는지, 방문을 전에 한 적이 있는지)
            if 0 <= ni < n and 0<= nj < n and not visited[ni][nj]:
                #응용 : 미로라면 1인 곳은 탐색할 수 없다고 추가로 넣어주면 됨

                #탐색이 가능한 위치면
                visited[ni][nj] = 1
                # 방문 체크를 하고
                queue.append((ni,nj))
                # 큐에 다음에 탐색을 하기 위해 큐에 다음 위치를 추가

n = 10
bfs(5,5,10) #시작위치는 (5,5), 2차원 배열의 크기는 10*