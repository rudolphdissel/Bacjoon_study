from itertools import permutations, combinations
n=int(input())
a=list(map(int,input().split()))
b=list(permutations(a))
board=[]
for i in b:
    score=0
    for j in range(n-1):
        t=i[j]-i[j+1]
        if t<0:
            t*=-1
        score+=t
    board.append(score)
print(max(board))