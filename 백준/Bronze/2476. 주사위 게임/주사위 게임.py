N=int(input())
max_score=0
for i in range(N):
    a,b,c= map(int,input().split())
    if a==b and b==c:
        score= 10000+a*1000
    elif a==b:
        score=a*100+1000
    elif b==c:
        score=b*100+1000
    elif a==c:
        score=c*100+1000
    else:
        score=max(a,b,c)*100
    if score>max_score:
        max_score=score
print(max_score)