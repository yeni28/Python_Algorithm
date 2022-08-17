# A~G -> 0~6
#행번호를 정점번호로 해서 인접인 것만 표시하는 리스트

adjList = [[1,2],        #0
           [0, 3, 4],    #1 저장된 순서가 정렬안되어 있다면 손으로 따라가기 어려울 것
           [0, 4],       #2
           [1, 5],       #3
           [1, 2, 5],    #4
           [3, 4, 6],    #5
           [5]]          #6

def dfs(v, N):
    # visited = [0] * N #정점의 개수 N  #visited 생성
    # stack = [0] * N # stack 생성
    top = -1
    print(v)       # 방문
    visited[v] = 1 # 시작점 방문 표시
    while True:
        for w in adjList[v]: #if (v의 인접 정점 중 방문 안 한 정점w가 있으면)
            if visited[w] == 0:
                top += 1        #push(v);
                stack[top] = v
                v = w           # v <- w;(w에 방문)
                print(v)        # 방문
                visited[w]  = 1 #visited[w] <- true;
                break
        else:                   # w가 없으면
            if top != -1:       # 스택이 비어있지 않은 경우
                v = stack[top]  # pop에 해당
                top -= 1
            else:               #스택이 비어있으면
                break           #while 종료

N = 7
visited = [0] * N #정점의 개수 N  #visited 생성
stack = [0] * N # stack 생성 stack: [1,0,2,4,5,0,0]
dfs(1, N)
print()