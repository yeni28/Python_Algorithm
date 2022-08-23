T = 10
num_list = []
for tc in range(10):
    num = int(input())
    num_list.append(num)
remain = []
for i in range(10):
    if not (num_list[i] % 42) in remain:
        remain.append(num_list[i] % 42)

print(len(remain))




