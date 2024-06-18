import sys
num_list=[]
K, N = map(int,sys.stdin.readline().split())
for _ in range(K):
    num_list.append(int(sys.stdin.readline()))
start=1
num_list.sort()
end= num_list[-1]

while start<=end:
    mid = (start+end)//2
    lines=0
    for i in num_list:
        lines+=i//mid
    if lines>=N:
        start=mid+1
    else:
        end=mid-1
print(end)
    

