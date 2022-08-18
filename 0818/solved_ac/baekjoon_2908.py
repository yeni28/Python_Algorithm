A,B = input().split()

a = A[::-1]
b = B[::-1]

if int(a) > int(b):
    print(a)
if int(a) < int(b):
    print(b)

