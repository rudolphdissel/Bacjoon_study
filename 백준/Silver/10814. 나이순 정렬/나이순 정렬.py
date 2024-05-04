N=int(input())
attend=[]
for i in range(N):
    a,b=input().split()
    attend.append((int(a),b))
attend=sorted(attend,key=lambda x:x[0])
for i in attend:
    print(i[0],end=" ")
    print(i[1])
    
    