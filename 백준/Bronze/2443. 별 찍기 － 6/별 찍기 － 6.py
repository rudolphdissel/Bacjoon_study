N=int(input())
a=[]
b=[]
c=[]
for i in range(N):
    a.append(" "*i)
for j in range(2*N-1,0,-2):
    b.append("*"*j)
for l in range(N):
    print(a[l]+b[l])
