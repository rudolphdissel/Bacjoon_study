import sys
munza=[]
N=int(sys.stdin.readline())
for i in range(N):
    munza.append(sys.stdin.readline().strip())
munza=list(set(munza))
munza.sort()
munza.sort(key=len)
for i in munza:
    print(i)