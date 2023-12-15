#3003
# a,b,c,d,e,f=map(int,input().split())
# user_input=[a,b,c,d,e,f]
# final_output= [1-a,1-b,2-c,2-d,2-e,8-f]
# for i in final_output:
#     print(i, end=" ")

# right = [1,1,2,2,2,8]
# comp = list(map(int,input().split()))
# for i in range(6):
#     need = right[i]-comp[i]
#     print(need,end=" ")

#2444 (별찍기-7)
# count=int(input())
# a=[]
# for i in range(count-1):
#     a.append(" "*(count-(i+1))+"*"*(2*i+1))
# b=a[::-1]
# a.append("*"*(2*count-1))

# for j in a:
#     print(j)
# for k in b:
#     print(k)

# n = int(input())
# for i in range(1, n + 1):
#     print(' '*(n-i)+'*'*(2*i-1))
# for j in range(n - 1, 0, -1):
#     print(' '*(n-j)+'*'*(2*j-1))

#몰랐는데 range함수에서 3번째 값을 -1로 쓰면 대입할 숫자를 앞에 숫자에서 -1씩 줄이면서 대입할 수 있다.
#줄이면서 대입할 수 있다면, 위 문제와 같이 i를 대입할수록 숫자가 작아지는 case를 처리할 때 좋다.

#10988 팰린드롬인지 확인하기
# a=input()
# b=[]
# for i in a:
#     b.append(i)
# c=b[::-1]
# if b==c :
#     print(1)
# else :
#     print(0)

#[::1]이라는 것도 있다. 그냥 0부터 1씩 게속 가는거다. 이렇게 하면 더 쉽게 위 문제를 해결 가능하다.

#1157 단어공부
#1
# a=input()
# a=a.lower()
# state="not_same"
# max=0
# ref='abcdefghijklmnopqrstuvwxyz'
# for i in ref:
#     c=a.count(i)
#     if c>max:
#         max=c
#         state=i
#     elif c==max:
#         state="same"
# if state=="same":
#     print("?")
# else :
#     print(state.upper())





#2941 크로아티아 알파벳
# a=input()
# ref=["c=", "c-","dz=", "d-", "lj", "nj", "s=", "z="]
# for i in ref:
#     if i in a:
#         a=a.replace(i,"p")
# print(len(a))
          
#1316 그룹 단어 체커
# N=int(input())
# group_word=0
# for i in range(N):
#     word=input()
#     for i in word:
#         if word.count(i)>=2:
#             val=word.count(i)
#             if not i*val in word:
#                 group_word-=1
#                 break
#         elif word.count(i)==1:
#             continue
#     group_word+=1
# print(group_word)

#25206 너의 평점은
# score_all=0
# exception=0
# all_credit=0
# for i in range(20):
#     a,b,c = input().split()
#     b=float(b)
#     if c=="A+":
#         score=4.5
#     elif c=="A0":
#         score=4.0
#     elif c=="B+":
#         score=3.5
#     elif c=="B0":
#         score=3.0
#     elif c=="C+":
#         score=2.5
#     elif c=="C0":
#         score=2.0
#     elif c=="D+":
#         score=1.5
#     elif c=="D0":
#         score=1.0
#     elif c=="F":
#         score=0.0
#     else:
#         score=0
#         exception+=b
#     all_credit+=b
#     score_all+=score*b
# score_avr=score_all/(all_credit-exception)
# print(score_avr)

#이 문제 같은 경우, dict를 쓰면 if문을 쓸 필요가 없다.

dic = {'A+':4.5, 'A0':4.0}
print(dic['A+'])




