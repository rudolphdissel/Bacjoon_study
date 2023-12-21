import sys
import math
N=int(sys.stdin.readline())
num_list=[]
num_dict={}
for i in range(N):
    num=int(sys.stdin.readline())
    if num not in num_dict:
        num_dict[num] =1
    else:
        num_dict[num]+=1
    num_list.append(num)
maxN=max(num_dict.values())
# a= [x for x in range(5) if x==3]
mode = [k for k, v in num_dict.items() if maxN == v]
mode.sort()

#산술평균
j_sum=0
for j in num_list:
    j_sum+=j
j_avg=j_sum/N
print(round(j_avg))

#중앙값
num_list.sort()
index_middle=math.ceil(len(num_list)/2)
print(num_list[index_middle-1])

#최빈값
print(mode[1] if len(mode) >1 else mode[0])


#범위
print(max(num_list)-min(num_list))