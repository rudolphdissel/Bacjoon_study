perfect=[]
M=int(input())
N=int(input())
for i in range(M,N+1):
    ar=round(i**0.5,1)**2
    if ar==i:
        perfect.append(i)
if perfect==[]:
    print(-1)
else:
    print(sum(perfect))
    print(min(perfect))