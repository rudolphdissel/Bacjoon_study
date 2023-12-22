import sys
N=int(sys.stdin.readline())
ans=0
#1부터 N까지 다 확인할거야
for i in range(N):
    m=str(i)
    if ans!=0:
        break
    bubunsum=0
    for j in range(len(m)):
        bubunsum+=int(m[j])
    bunsum=bubunsum+i
    if bunsum==N:
        ans=i

if ans==0: 
    print(0)
else:
    print(ans)