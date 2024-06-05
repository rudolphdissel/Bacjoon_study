T=int(input())
for i in range(T):
    k=int(input())
    n=int(input())
    ans=[]
    first=[x for x in range(1,15)]
    ans.append(first)
    for i in range(k):
        temp=[]
        for j in range(14):
            temp.append(sum(ans[i][0:j+1]))
        ans.append(temp)
    print(ans[k][n-1])
