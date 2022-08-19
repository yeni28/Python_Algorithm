
T = int(input())

for tc in range(1,T+1):
    tc, road = map(int, input().split())

    adjList = []
    for node in range(0, road * 2, 2):
        adjList.append(list(map(int, input().split())))

    graph = [[0] * (V+1) for _ in range(V+1)]
    for adj in adjList:
        graph[adj[0]][adj[1]] = 1 #2차원 배열을 통해 연결 표시

    visited = [0] * 100
    stack = []
    S = 0
    visited[S] =

    while True:
        for i in range(1, V+1): #노드가 1에서부터 시작하니 범위 1~V+1
            if graph[v][i] == 1 and visited[i] == 0:
                #만약 v행(처음 시작점이 행이됨)의 i열이 연결되어있고
                # 방문했던 장소가 아니라면
                visited[i] = 1
                #방문했다고 표시해주고
                stack.append(v)
                #스택에 방문 경로를 저장해준다.
                v = i
                # 시작점을 새로운 i로 교환해준다.
                break
        else:
            if stack:
                #만약 if조건에 걸리지 않았다면(이동할 수 없다면)
                #그리고 스택에 값이 들어있다면(이전의 이동경로)
                v = stack.pop()
                #출발점은 이전 경로로 돌아간다.
            else:
                break
                #스택에 값이없다면(어디로든 못가는 상황)
                #끝낸다.

    print(f'#{tc} {visited[G]}')
    #visited[G]가 도착점의 방문여부이므로 연결되었다면 1, 아니라면 0이 뜰 것


