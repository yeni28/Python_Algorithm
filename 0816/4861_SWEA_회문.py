T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    # nxn의 글자 받기
    arr = [list(input()) for _ in range(n)]

    aws = ""
    # 가로 회문 탐색
    for i in range(n):
        for j in range(n): #인덱스 범위 조심
            word_row = ""
            for k in range(m):
                if j+k <= n-1:
                    word_row += arr[i][j+k]
            if word_row == word_row[::-1] and len(aws) == m:
                aws = word_row

    # 세로 회문 탐색
    for i in range(n):
        for j in range(n):
            word_col = ""
            for k in range(m):
                if j + k <= n - 1:
                    word_col += arr[j + k][i]
            if word_col == word_col[::-1] and len(aws) == m:
                aws = word_col


    print(f'#{tc} {aws}')