N = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 10
num_list = ""



for k in range(len(num_list)):
    if k + 1 < len(num_list):
        if num_list[k] <= num_list[k+1]:
            num_len += 1
        elif num_list[k] >= num_list[k+1]:
            num_len2 += 1
        else:
            print(2)

if max_len < num_len:
    max_len = num_len
elif max_len < num_len2:
    max_len = num_len2
print(max_len)



