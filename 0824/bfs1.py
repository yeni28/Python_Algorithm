

def bfs(v, N): #필요한 것 : 시작정점(v), 마지막 정점 번호(N)
    visited = [0] * (N+1) # visited 생성
    q = [] # 큐 생성
    q.append(v)# 시작점 인큐
    visited[v] = 1 # 시작점 방문 표시

    while q: # 큐가 비어있지 않으면
        v = q.pop(0) # 디큐 / 디큐한 다음에 처리하는 것이 기본 형식이다.
        print(v)     #visit(v)
        for w in adjList[v]:# 인접하고 미방문(인큐되지 않은) 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

V, E = map(int,input().split())
N = V + 1 # 여기서의 N은 개수에요! 헷갈리지 마세요! (N 정점 개수)
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a) #화살표가 없다면 둘다 마주볼 수 있도록

bfs(0, V)
