N= int(input())
leng =0
ans=[]
# if N==1:
#     print(3)
#     print(1,1,0)
# else:
for k in range(N//2-1, N+1):
    my_list=[N,k]
    i=1
    while True:
        c = my_list[i-1] - my_list[i]
        if c>=0:
            my_list.append(c)
            i+=1
            if c==0:
                break
        else:
            break
    if len(my_list)>=leng:
        leng=len(my_list)
        ans=my_list
print(leng)
result = ' '.join(map(str, ans))
print(result)