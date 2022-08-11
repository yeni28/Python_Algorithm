di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 3
M = 4

arr = [[1,2,3,4],[4,5,6,8]]
for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M:
                print(ni,nj)
# 만약 두 칸을 건너 돌려면?

for i in range(N):
    for j in range(M):
        for d in range(1,3):
            for k in range(4):
                ni = i + di[k]*d #처음에는 1칸 옆, 그다음은 2칸 옆돌기
                nj = j + dj[k]*d
                if 0<=ni<N and 0<=nj<M:
                    print(ni,nj)


#other

for i in range(N):
    for j in range(M):
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M:
                print(ni,nj)


