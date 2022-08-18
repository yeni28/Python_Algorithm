def stick(N):
    paper[1] = 1
    paper[2] = 3
    for i in range(1, N):
        paper[i] =  2 * paper[i-1] + paper[i - 2]


print(paper[30])






# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     board = [[0] * N for _ in range(20)]
#     print(f'#{tc} {paper[N]}')