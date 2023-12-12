#1546
# max=0
# sum=0
# N=int(input())
# a=list(map(int,input().split()))
# for i in range(N):
#     if a[i]>max:
#         max=a[i]
# for i in a:
#     i=i/max*100
#     sum=sum+i
# print(sum/N)

#max함수를 쓰면 더 쉽게 가능.

#27886
# S=input()
# i=int(input())
# print(S[i-1])

#중요한 문법사실. 문자열은 리스트처럼 여겨진다.

#2743
# a=input()
# print(len(a))

#9086
# T=int(input())
# for i in range(T):
#     text=input()
#     print(text[0]+text[-1])

#11654
# aski=input()
# print(ord(aski))

#11720
# sum=0
# N=int(input())
# num=input()
# for i in range(N):
#     sum = sum+int(num[i])
# print(sum)

#10809
# S=input()
# ans=[-1]*26
# ref='abcdefghijklmnopqrstuvwxyz'
# for i in S:
#     ans[ref.index(i)] = S.index(i)
# print(ans)

#2675
# ans=[]
# T=int(input())
# for i in range(T):
#     num,retry= input().split()
#     numi=int(num)
#     for j in retry:
#         ans.append(j*numi)
#     ans.append("\n")
# for k in ans:
#     print(k, end="")

#1152
# ans=0
# A=input()
# if A[0] == " ":
#     ans-=1
# if A[-1] == " ":
#     ans-=1
# for i in A:
#     if i==" ":
#         ans+=1
# rans=ans+1
# print(rans)

#훨씬 쉬운 방법
# s= list(input().split())
# print(s)