n=int(input())
map_array= [[0]*100 for _ in range(100)]

for _ in range(n):
    x,y= map(int,input().split())
    for i in range(y,y+10):
        y_=i
        for j in range(x,x+10):
            x_=j
            if map_array[y_][x_]==0:
                map_array[y_][x_]=1
            else:
                continue
ans=0
for i in range(100):
    ans+=sum(map_array[i])
print(ans)
    