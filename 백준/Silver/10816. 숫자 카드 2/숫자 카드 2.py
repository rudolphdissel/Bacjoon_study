import sys
N=int(sys.stdin.readline())
given_num=list(map(int,(sys.stdin.readline().split())))
M=int(input())
target_num = list(map(int,(sys.stdin.readline().split())))

number_table={}

for i in given_num:
    if i in number_table.keys():
        number_table[i]+=1
    else:
        number_table[i]=1

answer=[]
for i in target_num:
    if i in number_table.keys():
        answer.append(number_table[i])
    else:
        answer.append(0)
        

# answer라는 리스트에 있는거를 str로 바꾸고, 그 리스트를 문자열로 결합하는데 " "로
print(" ".join(map(str,answer)))