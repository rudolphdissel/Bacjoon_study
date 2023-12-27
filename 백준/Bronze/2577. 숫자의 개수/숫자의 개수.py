a=int(input())
b=int(input())
c=int(input())
num=str(a*b*c)
num_list=[int(x) for x in num]

for i in range(10):
    print(num_list.count(i))