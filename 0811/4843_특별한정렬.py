T = int(input())

for tc in range(1,T+1):
    N = int(input())
    a = list(map(int, input().split()))

    for k in range(N - 1):
        if k % 2 == 0:
            maxIndex = k
            for j in range(k+1, N):
                if a[maxIndex] < a[j]:
                    maxIndex = j
            a[k], a[maxIndex] = a[maxIndex], a[k]
        else:
            minIndex = k
            for j in range(k+1, N):
                if a[minIndex] > a[j]:
                    minIndex = j
            a[k], a[minIndex] = a[minIndex], a[k]

    sort_num = ""
    # for n in a:
    #    sort_num += str(n) + " "

    for num in range(10):
        sort_num += str(a[num]) + " "

    print(f'#{tc} {sort_num}')

