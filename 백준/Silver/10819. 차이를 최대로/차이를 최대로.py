from itertools import permutations, combinations
n=int(input())
a=list(map(int,input().split()))
b=list(permutations(a))
ans=0
for i in b:
    t=0
    for j in range(n-1):
        t+=abs(i[j]-i[j+1])
    ans=max(ans,t)
print(ans)

#1. abs라는 함수가 있다.
#2. 나처럼 리스트에 담지말고, 그 때 그 때 max를 뽑아서 비교하면 메모리 절약이 가능하다.