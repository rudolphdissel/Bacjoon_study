n=int(input())
weban=0
car= list(map(int,input().split()))
for i in car:
    if i==n:
        weban+=1
print(weban)