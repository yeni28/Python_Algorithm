def num_sort(numbers,N):
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    num_sort(numbers, N)
    print(f'#{tc} {numbers[N-1]-numbers[0]}')


#other sol


#List = [11,2,3,4,9,10] #최신화 시키면서 비교
# maxV = # 주어진 범위에서 제일 작은 수 혹은 첫 번째 수를 사용해도 된다.
# minV = #최솟값을 설정할 때는 임의의 수가 아닌 리스트 안에 있는 것을 하나 정하거나, 혹은 최대의 값을 넣는다. > 리스트 안의 값을 찾기 위해
# 아무 값이 아닌 문제에서 주어진 범위 혹은 리스트 안의 값들에서 골라야한다는 것을 기억하자!


# for num in List:
    # if minV > num:
    # minV = num