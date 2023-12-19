#이코테 그리디 3번문제
# S=input()
# result=0
# for i in S:
#     j=int(i)
#     if result==0 or result==1 or j==1 or j==0:
#         result+=j
#     else:
#         result*=j
# print(result)

# #동빈나님의 답

# data=input()
# result=int(data[0])
# for i in range(1,len(data)):
#     num = int(data[i])
#     if num<=1 or result<=1:
#         result+=num
#     else:
#         result*=num
# print(result)

#모험가 길드 문제
#입력받기
#내 답변
# N=int(input())
# fear=list(map(int,input().split()))
# group=0
# namusi=0
# for i in range(1,N+1):
#     if i in fear:
#         amount=fear.count(i)
#         group+=(amount+namusi)//i
#         namusi+=amount%i
# print(group)

# n= int(input())
# data=list(map(int,input().split()))
# data.sort()

# result=0
# count=0

# for i in data:
#     count+=1
#     if count>=i:
#         result+=1
#         count=0
# print(result)

#10162 전자레인지
#600, 60, 10
#입력 받기
# import sys
# T=int(sys.stdin.readline())
# if T%10==0:
#     for i in [300,60,10]:
#         print(T//i, end= " ")
#         T=T-i*(T//i)
# else :
#     print(-1) #불가능 선언.

#11047 동전 0
#입력 받기
# coin_list=[]
# coin_amount=0
# N,K = map(int,input().split())
# for i in range(N):
#     coin=int(input())
#     coin_list.append(coin)
# coin_list.reverse() #mehtod를 이렇게 먹이면 데이터가 변한다.
# for j in coin_list:
#     coin_amount+=K//j
#     K=K-(K//j*j)
# print(coin_amount)

##정렬 문제연습##
#2750 수 정렬하기
# N=int(input())
# num_list=[]
# for i in range(N):
#     num=int(input())
#     num_list.append(num)
# num_list.sort()
# for j in num_list:
#     print(j)

#2752 세수정렬
a,b,c=map(int,input().split())
d= [a,b,c]
d.sort()
for i in d:
    print(i, end=" ")