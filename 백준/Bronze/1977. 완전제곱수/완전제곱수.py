perfect=[]
M=int(input())
N=int(input())
for i in range(M,N+1):
    for j in range(1,i+1):
        if j**2==i:
            perfect.append(i)
if perfect==[]:
    print(-1)
else:
    print(sum(perfect))
    print(min(perfect))