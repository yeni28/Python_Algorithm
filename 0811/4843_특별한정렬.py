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


    #other sol #깃랩 올라온 것 참고해서 정리하기

    T =

    index = 0 #바꿀 원소의 인덱스
    i = 0 # 탐색을 시작할 위치

    for ni in range(10):
        #정렬시작
        for j in range(i, n): #최대값 또는 최솟값을 찾기 시작
            if ni % 2 == 0 and numbers[j] > numbers[index]:
                #최대값의 인덱스
                index = j
            if ni % 2 == 1 and numbers[j] > numbers[index]:
                index = j
                #최소값의 인덱스

            i += 1

            for i in range(10):
                print()

