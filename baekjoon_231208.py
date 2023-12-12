#3052
# a=[0]*10
# b=[]
# for i in range(10):
#     a[i] = int(input())
#     a[i] = a[i]%42
#     if a[i] in b:
#         continue
#     else:
#         b.append(a[i])
# print(len(b))

#set자료형을 이용해서 푸는 방법도 있다. set자료형은 중복을 허용하지 않아서, set처리를 해주면 중복된게
#자동으로 사라진다고한다.

#10811
# N,M = map(int,input().split())
# c=[x+1 for x in range(N)]
# for i in range(M):
#     a,b = map(int,input().split())
#     new_list=c[a-1:b]
#     new_list.reverse()
#     c[a-1:b]=new_list
# for i in c :
#     print(i, end= " ")