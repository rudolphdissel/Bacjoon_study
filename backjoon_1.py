#1001
###
# a, b = map(int, input().split())
# print(a+b)
###

#input에 split이라는 method는 2개 이상의 값을 입력받아서, 공백을 기준으로 나눈다. 입력받은 만큼 저장할 변수가 있어야겠지?
#map이라는 함수도 처음보는데, 이게 리스트나 튜플의 요소에다가 함수를 치는것이다. 그게 map이다. 핵심은 리스트나 튜플에 친다는거다. int를 list에는 못감싸니까 이렇게 한다.


#1002
# a,b = map(int,input().split())
# print(a-b)

#10998
# a,b = map(int,input().split())
# print(a*b)

#1008
# a,b = map(int,input().split())
# print(a/b)

#10869
# a,b = map(int,input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b) 
# print(a%b)
#몫을 구해야되는데 나누기결과를 구해서 오래걸렸다...

#10926
# surprise=input()+"??!"
# print(surprise)
#? ㅋㅋㅋ

#18108
# print(int(input())-543)

#10430
# a,b,c = map(int,input().split())
# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)

#2588
# a= int(input())
# b= input()
# c=[]
# for i in b:
#     c.append(i)
# print(a*int(c[2]))
# print(a*int(c[1]))
# print(a*int(c[0]))
# print(a*int(b))
#놀랍게도 for문은 list뿐만 아니라 문자열과도 사용할 수 있다.

# a=int(input())
# b=input()
# c=list(b)
# print(a*int(c[2]))
# print(a*int(c[1]))
# print(a*int(c[0]))
# print(a*int(b))
#그냥 list 함수 쓰면 되네...

###

#11382
# a,b,c = map(int,input().split())
# print(a+b+c)

#10171
# print("\\    /\\ \n )  ( \')\n(  /  )\n \\(__)|")

#10172
print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")