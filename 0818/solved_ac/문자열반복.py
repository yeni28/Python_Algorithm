T = int(input())
for tc in range(T):
    r, s = input().split()
    result = ""
    for i in s:
        result += i * int(r)
    print(result)

