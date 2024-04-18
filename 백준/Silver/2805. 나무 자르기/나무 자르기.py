import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
start,end=1,max(trees)

while start<=end:
    mid= (start+end) //2
    cnt=0
    #나무 자르기
    for tree in trees:
        if tree>mid:
            cnt+=tree-mid
    if cnt>=m:
        start=mid+1
    else:
        end=mid-1
print(end)