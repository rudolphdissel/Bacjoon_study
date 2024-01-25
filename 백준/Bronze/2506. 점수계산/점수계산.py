N=int(input())
sheet=list(map(int,input().split()))
bonus=0
score=0
for i in sheet:
    if i==1:
        score=score+bonus+1
        bonus+=1
    elif i==0:
        bonus=0
print(score)