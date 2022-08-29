T = int(input())


## 인덱스 0,1 좌표부터 인덱스 2,3 좌표까지 인덱스 4가 가리키는 색으로 색칠한다.


for tc in range(1, T+1):
    N = int(input())
    # for area in range(N):
    area_list = [list(map(int, input().split())) for _ in range(N)]
    cnt = [[0] * 10 for _ in range(11)]
    purple = 0
    for idx in range(N):
        x1 = area_list[idx][0]
        y1 = area_list[idx][1]
        x2 = area_list[idx][2]
        y2 = area_list[idx][3]
        color = area_list[idx][4]
        di = range(x2)
        dj = range(y2)

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if cnt[i][j] != 0:
                    cnt[i][j] = 3
                    purple += 1
                else:
                    cnt[i][j] = color

    print(f'#{tc} {purple}')
