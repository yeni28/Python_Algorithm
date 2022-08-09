T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # M구간 만큼 본인 값에서 더하는 구간합을 만든다.
    sum_list = []
    max_sum = 0
    min_sum = int(1e9)
    for num_idx in range(N-M+1):
        #M까지의 합
        num_sum = 0
        for i in range(num_idx, num_idx + M):
            num_sum += numbers[i]
        if max_sum < num_sum:
            max_sum = num_sum
        if min_sum > num_sum:
            min_sum = num_sum

        # sum_list.append(num_sum)

    print(f'#{tc} {max_sum - min_sum}')












