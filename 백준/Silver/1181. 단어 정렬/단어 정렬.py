munza=[]
new=[]
N=int(input())
for i in range(N):
    munza.append(input())
munza=list(set(munza))
for i in munza:
    new.append((len(i),i))
new.sort()
for i in new:
    print(i[1])