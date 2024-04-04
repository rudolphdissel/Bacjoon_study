n = int(input()) #5
num = n
count = 0

while True:
    a = num//10 #0
    b = num%10 #5
    c = (a+b)%10 #5
    num = (b*10)+c #5
    
    count+=1
    if(num==n):
        break

print(count)