N=int(input())
for i in range(N):
    a=input()
    while True:
        if "()" in a:
            a=a.replace('()','')
        else: 
            break
    if a=="":
        print("YES")
    else:
        print("NO")