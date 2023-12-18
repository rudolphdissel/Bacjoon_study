# import time
# start = time.time()
# #1 나의 정답.
# count=0
# N,K= map(int,input().split())
# while N!=1:
#     if N%K==0 and N>=K:
#         N=N/K
#         count+=1
#     else :
#         N=N-1
#         count+=1
# print(count)
# print(time.time() -start)

#2 동빈나님의 정답.
# n, k = map(int,input().split())
# result =0
# while True:
#     target=(n//k)*k
#     result+=(n-target)
#     n=target
#     if n<k:
#         break
#     result+=1
#     n//=k
# result+=(n-1)
# print(result)

#2720 세탁소 사장 동혁
# T=int(input())
# a=[]
# ans=[]
# for i in range(T):
#     b=int(input())
#     a.append(b)
# for j in a:
#     quater=0
#     dime=0
#     nickel=0
#     penny=0
#     while j!=0:
#         if j>=25:
#             j=j-25
#             quater+=1
#         elif j>=10:
#             j=j-10
#             dime+=1
#         elif j>=5:
#             j=j-5
#             nickel+=1
#         else:
#             j=j-1
#             penny+=1
#     ans.append([quater, dime, nickel, penny])
# for k in ans:
#     for l in k:
#         print(l, end=" ")
#     print("")
    
T=int(input())
for i in range(T):
    b=int(input())
    quater=b//25
    b=b%25
    dime=b//10
    b=b%10
    nickel=b//5
    b=b%5
    penny=b
    print(quater,dime,nickel,penny, end= " ")
#저 위에 내가 저저 쓴거 저체가 반복문이네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ.....
T=int(input())
for i in range(T):
	b = int(input())
	for i in [25, 10, 5, 1]:
		print(b//i, end=' ')
		b = b%i