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
count=0
for i in target_num:
    count+=1
    if count!=len(target_num):
        if i in number_table.keys():
            print(number_table[i], end=" ")
        else:
            print(0, end=" ")
    else:
        if i in number_table.keys():
            print(number_table[i], end="")
        else:
            print(0, end="")
    
