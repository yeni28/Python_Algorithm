N = 3 #행
M = 4 #열
# N개의 원소를 갖는 0으로 초기화된 1차원 배열
arr1 = [0] * N

# 크기가 NxM이고 0으로 초기화 된 2차원 배열

arr2 = [[0] * M for _ in range(N) ]
#arr2는 실제 배열 / 비어있음을 나타내는 숫자를 채워 넣어야한다.
arr2_1 = [[] * M for _ in range(N) ]
# 레퍼런스만 있는 것

# arr3 = [[0]*M]*N]의 경우 행을 하나 만들고 레퍼런스를 두 개 더하는 것이다.

arr3 = [[1],[2,3],[3,4,5]]
# 각 행의 크기가 동일하지 않아도 된다.
