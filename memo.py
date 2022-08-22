# arr = [[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [11, 22, 33, 44, 55],
#        [66, 77, 88, 99, 100]]
#     # 우 하 좌 상 우하 우상 좌상 좌하
# di = [0, 1, 0, -1, 1, -1, -1, 1]
# dj = [1, 0, -1, 0, 1, 1,-1,-1]
# result = []
# for i in range(5):  # 행
#     for j in range(5):  # 열
#         for dt in range(8):  # 델타
#             for distance in range(1, 4):  # 디스턴스
#                 if 0 <= i + di[dt]*distance < 5 and 0 <= j + dj[dt]* distance < 5:
#                     result.append(arr[i + di[dt]*distance][j + dj[dt]*distance])
#
# print(result)

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
print(arr)