
#1330
# a,b = map(int,input().split())
# if a>b :
#     print(">")
# elif a<b :
#     print("<")
# else:
#     print("==")

#9498
# a=int(input())
# if a>=90 :
#     print("A")
# elif a>=80 :
#     print("B")
# elif a>=70 :
#     print("C")
# elif a>=60:
#     print("D")
# else:
#     print("F")

#2753
# a=int(input())
# if a%4==0 and a%100!=0 :
#     print("1")
# elif a%4==0 and a%400==0 :
#     print("1")
# else :
#     print("0")


# a=int(input())
# if a%4==0 and (a%100!=0 or a%400==0) :
#     print("1")
# else :
#     print("0")

#14681
# a=int(input())
# b=int(input())
# if a>0 and b>0 :
#     print("1")
# elif a<0 and b>0 :
#     print("2")
# elif a<0 and b<0 :
#     print("3")
# else:
#     print("4")

#2884
# a,b=map(int,input().split())
# if b>=45 :
#     print(a,b-45)
# elif b<45 and a!=0:
#     print(a-1,b+15)
# else :
#     print(23,b+15)
   
#2525
# a,b=map(int,input().split())
# c=int(input())
# if c>=60:
#     a+=c//60
#     b+=c%60
#     if b>=60:
#         a+=1
#         b-=60 
#     if a>=24:
#         a=a-24 
#     print(a,b) 
# else :
#   b+=c
#   if b>=60:
#     a+=1
#     b-=60
#   if a>=24:
#     a=a-24 
#     print(a,b)

#2480
# prize=0
# a,b,c = map(int,input().split())
# if a==b==c :
#   prize = a*1000+10000
# elif a==b or a==c or b==c:
#   if a==b or a==c:
#     prize= a*100+1000
#   else: 
#     prize= b*100+1000
# elif a>b>c or a>c>b:
#   prize=a*100
# elif b>a>c or b>c>a:
#   prize=b*100
# elif c>a>b or c>b>a:
#   prize=c*100
# print(prize)


#2739
# x= int(input())
# numbers=(1,2,3,4,5,6,7,8,9)
# for i in numbers:
#   print(f"{x} * {int(i)} = {int(i)*x}") 

#10950
# t=int(input())
# for i in range(1,t+1):
#   a,b=map(int,input().split())
#   print(a+b)

#8393
# summ=0
# n=int(input())
# for i in range(1,n+1):
#     summ= summ+i
# print(summ)

#25304
# sumA=0
# sumB = int(input())
# N = int(input())
# for i in range(1,N+1):
#     a,b = map(int,input().split())
#     sumA=sumA+a*b
# if sumA==sumB :
#     print("Yes")
# else:
#     print("No")

#25314
# out= "int"
# N=int(input())
# n=N//4
# for i in range(1,n+1):
#     out = "long "+out
# print(out)

#15552
# import sys
# T = int(sys.stdin.readline())
# for i in range(1,T+1):
#     a,b = map(int,sys.stdin.readline().split())
#     print(a+b)

#11021
# import sys
# T = int(sys.stdin.readline())
# for i in range(1,T+1):
#     a,b=map(int,sys.stdin.readline().split())
#     print(f"Case #{i}: {a+b}")

#11022
# import sys
# T = int(sys.stdin.readline())
# for i in range(1,T+1):
#     a,b=map(int,sys.stdin.readline().split())
#     print(f"Case #{i}: {a} + {b} = {a+b}")

#2438
# import sys
# star=""
# N=int(sys.stdin.readline())
# for i in range(1,N+1):
#     star=star+"*"
#     print(star)

#2439
# blank=" "
# import sys
# N=int(sys.stdin.readline())
# for i in range(1,N+1):
#     print(blank*(N-i)+"*"*i)

#10952
# playing="play"
# while playing=="play":
#     a,b=map(int,input().split())
#     if a==0 and b==0:
#         playing="stop"
#     el5se:
#         print(a+b)
    
#10951
# while True:
#     try:
#         a,b=map(int,input().split())
#         print(a+b)
#     except:
#         break

#10807
# score=0
# N=int(input())
# a=list(map(int,input().split()))
# b=int(input())
# print(a.count(b))

##굳이 이렇게 안해도 카운트 method만 쓰면 된다...
# for i in a:
#     if i==b:
#         score+=1
# print(score)

#10871
# N,X=map(int,input().split())
# num_list=list(map(int, input().split()))
# for i in range(N):
#     if num_list[i]<X:
#         print (num_list[i], end=" ")
        

#10818
# max_data=-1000001
# min_data=1000001
# N=int(input())
# num_list=list(map(int, input().split()))
# for i in range(N):
#     if num_list[i]>max_data:
#         max_data=num_list[i]
# for i in range(N):
#     if num_list[i]<min_data:
#         min_data=num_list[i]
# print(min_data,max_data)

#그냥 이거쓰면 해결되요...
# print(min(num_list), max(num_list))

#2562
# max_value=0
# for i in range(9):
#     now_value=int(input())
#     if now_value>max_value:
#         max_value=now_value
#         max_position=i+1
# print(max_value)
# print(max_position)

#10810
'''
#내가 짠 코드
N,M=map(int,input().split())
backet=[0 for x in range(N)] #길이가 N인 리스트를 만들어서 거기다 추가하는 방법을 쓰고 싶었다.
for each in range(M):
    i,j,k = map(int,input().split())
    for each in range(i-1,j):
        backet[each]=k
for each in backet:
    print(each, end=" ")
#아직 배열에 대한 기본기가 너무 부족한 것 같다. 그 동영상으로 내일은 공부하고 시작하자.

#다른 사람이 짠 코드
N,M = map(int,input().split(" "))

basket = [0]*N # 이 사람도 같은 발상인데, [0]*N도 되나보다.
for i in range(M):
    a,b,c = map(int,input().split(" "))
    basket[a-1:b] = [c]*(b-a+1) #슬라이싱 칠 발상은 했는데, 그 부분을 어떻게 대체하는지 몰랐다. *로 해결이 되는
    #것이다. 그렇다면 당연히 슬라이스 친 길이와 *뒤의 갯수가 다르면 오류가 뜨겠지? 와 오류가 안뜨네. 그냥 그 부분이
    #싹 들어내지고 새로운 값이 들어가는 개념이다. 이 때 리스트의 길이가 변할 수 도 있다.
for j in basket:
    print(j,end=" ")
'''
#10813
# N,M= map(int,input().split())
# list_start=[x+1 for x in range(N)]
# for i in range(M):
#     a,b=map(int,input().split())
#     c=list_start[b-1]
#     d=list_start[a-1]
#     list_start[a-1] = c
#     list_start[b-1] = d
# for i in list_start:
#     print(i, end=" ")
# 나보다 더 잘 한 사람을 보니... 이렇게 했다.
# a[x], a[y] = a[y], a[x]. 이렇게 하면 동시에 바꿀 수 있다. 

#5597
# 내 답안
# attend = []
# result= []
# for i in range(28):
#     attend.append(int(input()))
# for i in range(1,31):
#     if not i in attend :
#         result.append(i)
# print(result[0])
# print(result[1])

#다른 사람의 답안
# students = list(range(1,31)) # students 리스트에 1~30까지 숫자 넣음

# for i in range(28):          # 입력 28번 반복
#     num = (int(input()))     
#     students.remove(num)     # students 리스트에서 입력된 num 제거

# print(students[0])
# print(students[1])


#덕분에 list안에 어떤 요소가 있는지 어떻게 찾는지 배웠다. if i in attend이런식으로...
# 하지만 더 쉽게는 remove 메소드를 쓰면된다. 지금입력받을때마다... attend라는 리스트에 추가할
#필요가 없다. 그저 처음부터 1~30이 있는 리스트를 생각해놓고, 입력받은 숫자를 빼면된다.


