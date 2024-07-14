N=int(input())
pattern=input()
for i in range(len(pattern)):
    if ord(pattern[i])==42:
        first=pattern[:i]
        last=pattern[i+1:]


for i in range(N):
    flag=True
    test=input()
    if len(first)+len(last)>len(test):
        print("NE")
        flag=False
    if flag==True:
        for j in range(len(first)):
            if test[j]!=first[j]:
                print("NE")
                flag=False
                break
    if flag==True:
        for j in range(len(last)):
            if test[-j-1]!=last[-j-1]:
                print("NE")
                flag=False
                break
    if flag:
        print("DA")
        
    