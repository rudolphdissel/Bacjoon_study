from itertools import permutations, combinations

n=[]
for i in range(9):
    n.append(int(input()))

ans=list(combinations(n,7))
for i in ans:
    if sum(i)==100:
        i=list(i)
        i.sort()
        for j in i:
            print(j)
        break
    