N=int(input())
reque= list(map(int,input().split()))
resource= int(input())

reque.sort()

start=0
end=reque[-1]
answer=0
while start<=end:
    mid=(start+end)//2
    total=0
    for i in reque:
        if i>mid:
            total+=mid
        elif i<=mid:
            total+=i
    if total>resource:
        end=mid-1
    elif total<=resource:
        start=mid+1
print(end)
    