a=[]
N=input()
for i in N:
    a.append(int(i))
a.sort(reverse=True)
for i in a:
    print(i,end="")