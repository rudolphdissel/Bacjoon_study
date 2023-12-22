#2231 분해합

#입력받기
import sys
N=int(sys.stdin.readline())
ans=0
#1부터 N까지 다 확인할거야
for i in range(N):
    m=[int(x) for x in str(i)]
    if ans!=0:
        break
    bubunsum=sum(m)
    bunsum=bubunsum+i
    if bunsum==N:
        ans=i

if ans==0: 
    print(0)
else:
    print(ans)
