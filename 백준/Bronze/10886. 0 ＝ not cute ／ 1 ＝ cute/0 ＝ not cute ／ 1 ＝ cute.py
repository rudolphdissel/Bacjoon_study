N=int(input())
cute=[]
for i in range(N):
    cute.append(int(input()))
if cute.count(1)>cute.count(0):
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")
