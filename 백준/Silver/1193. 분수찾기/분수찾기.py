x=int(input())

hap=0
plus=0
m=0
while hap<x:
    plus+=1
    hap+=plus
if plus%2==0:
    m=x-(hap-plus)
    n=plus+1-m
else:
    n=x-(hap-plus)
    m=plus+1-n
print(f"{m}/{n}")
