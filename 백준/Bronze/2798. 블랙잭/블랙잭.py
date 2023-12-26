from itertools import combinations

max=0
N,M=map(int,input().split())
num_list=list(map(int,input().split()))
result=list(combinations(num_list,3))
for i in result:
    sum_blackjack=sum(i)
    if M>=sum_blackjack>max:
        max=sum_blackjack
print(max)