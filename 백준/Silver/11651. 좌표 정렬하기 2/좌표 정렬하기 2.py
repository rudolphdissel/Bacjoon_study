num_list=[]
N=int(input())
for i in range(N):
    a,b=map(int,input().split())
    num_list.append((b,a))
num_list.sort()
for i in num_list:
    print(i[1],i[0])