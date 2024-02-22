a=666
ans=[]
while a<=4000000:
    if '666' in str(a):
        ans.append(a)
    a+=1
print(ans[int(input())-1])