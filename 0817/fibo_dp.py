def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i - 1] + table[i-2]
    return # 끝 리턴 생략가능/ 명시 원칙

table = [0] * 101
fibo_dp(100)
print(table[20])



# N이 주어질 때, 피보나치(N)을 구하시오
# N은 0이상 100이하

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {table[N]}') #테이블을 미리 채워놨으니.. 테이블을 만들고 돌려가면서 쓰는것. N의 값이 크면 클수록 시간이 오래걸림. 범위는 얼마 안되는데 tc개수가 1000 이상이라면, 미리 구해놓고 가져다가 출력하는 것이 좋다.  