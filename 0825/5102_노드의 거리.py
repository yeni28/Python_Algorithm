def bfs(S,V,G):
    visited = [0] * (V + 1)
    q = []
    q.append(S)
    visited[S] = 1

    while q:
        S = q.pop(0)
        for w in adjList[S]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[S] + 1
    if visited[G] == 0:
        return 0
    else:
        return visited[G] - 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjList = [[] for _ in range(V+1)]
    for node in range(E):
        n1, n2 = list(map(int, input().split()))
        adjList[n1].append(n2)
        adjList[n2].append(n1)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S,V,G)}')