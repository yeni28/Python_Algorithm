S = input()
dict1 = {}

for i in range(len(S)):
    if S[i] not in dict1:
        dict1[S[i]] = i

# a부터 z 까지의 값을 인덱스? 뭐 그런걸로 가지는 걸 만들어서
# 그 안에 숫자를 넣을것임

# 만약 ord(97) 이 S에 있다면 dict1에서 값을 가져오고
# 없으면 -1 출력 할 것임
# 근데 순서대로 어떻게 정렬함?
alpha = ""
for num in range(97,123,1):
    if chr(num) in S:
        alpha += str(dict1[chr(num)]) + " "
    elif chr(num) not in S:
        alpha += str(-1) + " "

print(alpha)


#다른답
#
# S = input()
# for i in range(97,123):
#     print(S.find(chr(i)),end=" ")
